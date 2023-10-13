import requests
import json

# 試合IDとトークンを設定
match_id = 10  # 例として試合IDを設定
token = "abc12345"  # トークンを設定

# APIエンドポイントとクエリパラメータを設定
url = f"http://localhost:3000/matches/{match_id}"
query_params = {
    "token": token,
}

# ヘッダーを設定
headers = {
    "Content-Type": "application/json",
    "procon-token": token,
}

# 更新する情報を作成
turn = 1  # 更新する現在のターン数を設定
type_actions = 0  # 行動のタイプを設定
course_actions = 0  # 行動の方向を設定
masons_number = 1  # 行動する職人の番号を設定

# 職人の行動計画を設定
actions = [
    {
        "type": type_actions,
        "dir": course_actions,
        "mason": masons_number,
    }
]

# リクエストボディを作成
request_body = {
    "turn": turn,
    "actions": actions,
}

try:
    # APIリクエストを送信
    response = requests.post(url, json=request_body, params=query_params, headers=headers)
    # レスポンスを処理
    if response.status_code == 200:
        response_data = response.json()
        accepted_at = response_data.get("accepted_at")
        print(f"リクエストが受理されました。受理時刻: {accepted_at}")
    else:
        print(f"エラーが発生しました。ステータスコード: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("HTTPリクエストエラー:", e)