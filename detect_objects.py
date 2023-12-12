#!/usr/bin/env python
# coding: utf-8
#
# [FILE] detect_objects.py
#
# [DESCRIPTION]
#  ImageAIを利用して物体認識(Object Detection)を行うSlackアプリトップファイル
#
# [NOTES]
#  ImageAIについてはこちらを参照のこと
#  https://imageai.readthedocs.io/en/latest/detection/
#
#  既存のYOLOモデルファイルはこちらからダウンロードし、modelフォルダに配置する
#  https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/
#

import os, sys, time
from pathlib import Path
import requests
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from yolo_detect import yolo_detect_objects

# BOTトークンからアプリを初期化する
slack_token=os.environ.get("SLACK_BOT_TOKEN")
if slack_token == None:
    print("環境変数が設定されていません")
    sys.exit()
app = App(token=slack_token)

# アプリトークン
app_token = os.environ["SLACK_APP_TOKEN"]
# ユーザートークン：ファイルの内容を取得するため用いる
user_token = os.environ.get("SLACK_USER_TOKEN")
# ローカルフォルダー
local_folder = os.environ.get("LOCAL_FOLDER")
# YOLOモデルファイル
yolo_model_file = os.environ.get("YOLO_MODEL_FILE")

#
# [EVENT] message
#
# [DESCRIPTION]
#  次のメッセージを受信したときのリスナー関数
#   Unhandled request ({'type': 'event_callback', 'event': {'type': 'message', 'subtype': 'file_share'}})
#
@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

#
# [EVENT] file_shared
#
# [DESCRIPTION]
#  ファイルを共有したときに起動するリスナー関数
#
# [NOTES]
#  対応可能なファイルタイプ：jpg and png
#
@app.event("file_shared")
def file_shared(payload, client, ack, say):
    ack()
      
    # アップロードしたファイルのIDを取得する
    file_id = payload.get('file').get('id')
    
    # ファイル情報を取得する
    file_info = client.files_info(file = file_id).get('file')
    url = file_info.get('url_private')
    file_name = file_info.get('title')
    file_type = file_info.get('filetype')

    # 検出結果画像ファイルは処理をしない
    if file_name.startswith('Detected') == True:
        print("[INFO] 検出結果ファイルは処理しません")
        return
    
    if file_type != 'jpg' and file_type != 'png':
        say(f"サポートしていないファイル形式です： {file_type}")
        return
    
    # ファイルの内容を取得する
    resp = requests.get(url, headers={'Authorization': 'Bearer %s' % user_token})

    # 一時的にファイルをローカルフォルダーに保存する
    file_path = local_folder + "/" + file_name
    save_file = Path(file_path)
    save_file.write_bytes(resp.content)
    print("[SHARED FILE] " + file_path)
    
    # 出力する検出結果画像ファイル名を準備する
    annotated_image = local_folder + "/Detected-" + str(time.time()) + "-" + file_name
    
    print("[MODEL FILE] " + yolo_model_file)
    detected = yolo_detect_objects(file_path, annotated_image, yolo_model_file)
        
    if detected == False:
        say(f"対象物を認識できませんでした")
        return
    
    print("[DETECTED FILE] " + annotated_image)
    os.remove(file_path) 
    
    # 検出結果ファイルをアップロードする
    channel_id = payload.get('channel_id') 
    try:
        client.files_upload_v2(
            channel=channel_id,
            title="Detected - " + file_name,
            file=annotated_image,
            initial_comment="検出結果ファイルを添付します",
        )
        os.remove(annotated_image)
    except Exception as e:
        print(e)
    
#
# Start the Slack app
#
if __name__ == "__main__":
    print('⚡️Detection App starts...')
    SocketModeHandler(app, app_token).start()

#
# END OF FILE
#