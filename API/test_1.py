import json

# json.load関数を使ったjsonファイルの読み込み
with open('./openapi.json', 'r', encoding='utf-8') as f:
    di = json.load(f)

print(di['openapi'])  # deep insider：キーを指定して値を取得
