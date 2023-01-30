# slack-ml-detect

## Slack APIによるプログラミング　機械学習への応用編

Slack APIチュートリアル「NodeJSとSlack APIによるいまどきのネットワークプログラミング」の応用編として機械学習向けにアプリを公開する。

### 画像を認識する

Slackにアップロードした画像ファイルのどこに何があるかを認識する。

#### 必要なライブラリをインストールする

>$ pip install -r requirements.txt

#### 環境変数を設定する

- ファイルenv.tpl内のSLACK_BOT_TOKEN、SLACK_APP_TOKEN、SLACK_USER_TOKENに該当するトークン文字列を設定する
- 学習済みのYOLOモデルファイルは次のURLからダウンロードし、modelフォルダーに配置する
  [https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/]

- env.tplをenv.batに名前を変え、バッチを実行する
  >$ ren env.tpl env.bat
  >
  >$ env.bat

#### 画像ファイルから物体を認識する

- 一般的な対象物（人、乗り物、動物など）を特定する
- 起動方法
  >$ python detect_objects.py
- 画像ファイル（JPEGあるいはPNG）をアップロードする
- Slack画面に検出結果画像ファイルが添付される。そのファイルには検出された対象物の領域が枠とともに表示されていることを確認する。
