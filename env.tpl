@echo off
rem Slackアプリに用いる環境変数
rem
rem Botトークン
set SLACK_BOT_TOKEN=xoxb-***
rem アプリトークン
set SLACK_APP_TOKEN=xapp-***
rem ユーザートークン
set SLACK_USER_TOKEN=xoxp-***
rem ファイルを一時保存するフォルダー
set LOCAL_FOLDER=_temp
rem 物体検出モデルファイル
set YOLO_MODEL_FILE=model/yolov3.pt
rem ----- END OF FILE -----