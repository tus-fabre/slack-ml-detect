# slack-ml-detect

## Slack APIによるプログラミング　機械学習への応用編

Slack APIチュートリアル「NodeJSとSlack APIによるいまどきのネットワークプログラミング」の応用編として機械学習向けにアプリを公開する。

### 画像を認識する

Slackにアップロードした画像ファイルのどこに何があるかを認識する。

#### YOLOモデルファイルを配置する

学習済みのYOLOモデルファイルは次のURLからダウンロードし、modelフォルダーに配置する。
[https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/](
https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt/)

#### 必要なパッケージをインストールする

コマンドライン上で次のコマンドを起動し、依存するPythonパッケージをインストールする。

```bash
pip install -r requirements.txt
```

#### 環境変数を設定する

本アプリを起動するには環境変数の設定が必要である。env.tplファイルをenv.batバッチファイルとしてコピーし、以下の環境変数を定義する。

```bash
copy env.tpl env.bat
```

|  変数名  |  説明  |
| ---- | ---- |
|  SLACK_BOT_TOKEN  | Botユーザーとして関連付けられたトークン。対象Slackワークスペースのアプリ設定 > [OAuth & Permissions] > [Bot User OAuth Token]から取得する。xoxb-で始まる文字列。 |
|  SLACK_APP_TOKEN  | 全ての組織を横断できるアプリレベルトークン。対象Slackワークスペースのアプリ設定 > [Basic Information] > [App-Level Tokens]から取得する。xapp-で始まる文字列。 |
|  SLACK_USER_TOKEN  | アプリをインストールまたは認証したユーザーに成り代わってAPIを呼び出すことができるトークン。対象Slackワークスペースのアプリ設定 > [OAuth & Permissions] > [User OAuth Token]から取得する。xoxp-で始まる文字列。 |
|  LOCAL_FOLDER  | Slackにアップロードしたファイルを暫定的に保存するローカルフォルダーの名前 |
|  YOLO_MODEL_FILE  | 利用するYOLOモデルファイルのパス |

#### 画像ファイルから物体を認識する

- 一般的な対象物（人、乗り物、動物など）を特定する
- 起動方法

```bash
env.bat
python detect_objects.py
```

- 画像ファイル（JPEGあるいはPNG）をアップロードする
- Slack画面に検出結果画像ファイルが添付される。そのファイルには検出された対象物の領域が枠とともに表示されていることを確認する。

### 更新履歴

- 2023-12-12 ファイルアップロードをfiles_upload_v2()に変更
- 2023-02-01 初版
