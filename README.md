# Cutouter

複数の料理が写った写真を皿ごとに**切り分けて**、docomoの画像認識にかけるやつ。

## Setup
環境変数に以下を設定すること。
* `CUTOUTER_KEY`...このAPIのKEY、勝手に使われたら困るので
* `DOCOMO_APIKEY`...docomoのAPIKEY

また複数のライブラリを使用しているので、`pip install -r requirements.txt`を忘れないこと。

## Usage
`python app.py`でサーバーが起動する。
httpでルート直下に画像(jpg/jpeg/png)をポストすると、皿ごとの認識結果がjsonで返ってくる。

例) `curl -F file=@test.jpg` http://localhost:5000

レスポンス
```
現在検討中
```
