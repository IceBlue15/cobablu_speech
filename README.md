# コバブルおしゃべりプログラム

* コバブルアクリルスタンドとおしゃべりがしたくて作りました。

## 必要なPythonのバージョン

* Python 3.7+

#### インストール方法

* Windows版参考ページ : https://www.python.jp/install/windows/install.html

## 必要なパッケージ

* SpeechRecognition
* PyAudio
* playsound

#### インストール方法

* コマンドプロンプトにてコマンド

```
pip install パッケージ名
```

を実行して下さい。

* Windowsの環境によっては上記コマンドでPyAudioがインストールできない場合があります。その際はこちら( https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio )からOS(64bit or 32bit)とPythonのバージョンに合わせたwhlファイルをダウンロードしてインストールして下さい。(参考ページ : https://watlab-blog.com/2019/05/21/pyaudio-install/ )

## 事前準備

* このページ右上にある緑色のCodeボタンからDownload ZIPを選択し、ZIPファイルをダウンロードして下さい。

* ダウンロードしたZIPファイル(cobablu_speech-master.zip)を適当な場所に解凍して下さい。

* cobablu_speech-masterフォルダの中にmp3フォルダがあります。mp3フォルダ配下のフォルダ(bye, konbanha, ...)の内にmp3形式の音声ファイルを複数配置して下さい。

## 使い方

* コマンドプロンプト（Macの場合はターミナル）でcobablu_speech-masterフォルダに移動し、コマンド

```
python cobablu_speech.py
```

を実行して下さい。

* PCのマイクに向かって喋って下さい。認識したテキストの中にキーワードが含まれていれば対応するフォルダ内の音声ファイルが1つランダムで再生されます。

* （例：「おはよう」が含まれた文章を喋ると、ohayoフォルダ内の音声ファイルのいずれかが再生されます。）

* 「バイバイ」と喋るとプログラムが終了します。
