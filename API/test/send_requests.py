import requests
import json

# 試合IDとトークンを設定
match_id = 10  # 例として試合IDを設定
token = "abc12345"  # トークンを設定

# APIエンドポイントとヘッダーを設定
url = f"http://localhost:3000/matches/{match_id}?token=abc12345"
headers = {
    "Content-Type": "application/json",
    "procon-token": token,
}

# 更新する情報を作成
turn = 30  # 更新する現在のターン数を設定
type_actions = 0 # 行動のタイプを設定
course_actions = 0 # 行動の方向を設定
masons_number = 1 #行動する職人の番号を設定

# 職人の行動計画を設定
actions = [
    {
        "type": type_actions,  # 行動のタイプを設定（例: move, build, remove）
        "dir": course_actions,     # 行動の方向を設定
        "mason": masons_number,      # 職人の番号を設定
    },
    # 他の職人の行動計画も同様に設定
]

# リクエストボディを作成
request_body = {
    "turn": turn,
    "actions": actions,
}


request_body = {
    "turn": 30,
    "actions": [
        {
            "type": 0,
            "dir": 0
        }
    ]
}
# APIリクエストを送信
#response = requests.post(url, json=request_body, headers=headers)
response = requests.post(url, json=request_body, headers=headers)


# レスポンスを処理
if response.status_code == 200:
    response_data = response.json()
    accepted_at = response_data.get("accepted_at")
    print(f"リクエストが受理されました。受理時刻: {accepted_at}")
else:
    print(f"エラーが発生しました。ステータスコード: {response.status_code}")