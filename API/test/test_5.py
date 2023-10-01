import requests

# 試合IDとトークンを設定
match_id = 1000  # 例として試合IDを設定
token = "your_token_here"  # トークンを設定

# APIエンドポイントとヘッダーを設定
url = f"https://procon34system.kosen.work/matches/{match_id}"
headers = {
    "Content-Type": "application/json",
    "procon-token": token,
}

# 更新する情報を作成
turn = 200  # ターン数を設定
# 職人の行動計画を設定
actions = [
    {
        "type": "move",  # 行動のタイプを設定（例: move, build, remove）
        "dir": "up",     # 行動の方向を設定
        "mason": 1,      # 職人の番号を設定
    },
    # 他の職人の行動計画も同様に設定
]

# リクエストボディを作成
request_body = {
    "turn": turn,
    "actions": actions,
}

# APIリクエストを送信
response = requests.post(url, json=request_body, headers=headers)

# レスポンスを処理
if response.status_code == 200:
    response_data = response.json()
    accepted_at = response_data.get("accepted_at")
    print(f"リクエストが受理されました。受理時刻: {accepted_at}")
else:
    print(f"エラーが発生しました。ステータスコード: {response.status_code}")