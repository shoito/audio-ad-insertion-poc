# audio insertion検証

## 概要
pydubライブラリによる音源差し込みを検証する。

## 環境構築

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
brew install ffmpeg
```

※ffmpegのインストールにかなり時間がかかる。

## 検証
podcasts/eine.mp3 に ads/fanfare.mp3 が差し込まれて、out/inserted.mp3 が生成される。

```sh
python run.py
```
