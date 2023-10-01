# HTTP GETリクエストを使用して競技サーバーにアクセスする。
# リクエストとは、他方へ送信する要求メッセージなどのこと
import requests


server_url = "https://procon34system.kosen.work"# サーバーのURL
token_file = "C:/Users/kxiyt/Desktop/token.txt"
with open(token_file, encoding="UTF-8") as f:
    f_text = f.read()
token_text = f_text

# SSL証明書の検証を無効にする
requests.packages.urllib3.disable_warnings()

try:
    proxies = {
        "http":None,
        "https":None
    }
    # サーバーから試合状態を取得
    #response = requests.get(f"{server_url}/state?token={token_text}", verify=False, proxies=proxies)
    response = requests.get(f"{server_url}/state?token={token_text}")

    if response.status_code == 200 or response.status_code == 201 or response.status_code == 404:
        game_state = response.json()
        print("試合の状態を取得しました。（status_code == {response.status_code}）")
        print(game_state)
        
    else:
        print(f"エラーが発生しました。（status_code == {response.status_code}）")

except requests.exceptions.RequestException as e:
    print("HTTPリクエストエラー:", e)