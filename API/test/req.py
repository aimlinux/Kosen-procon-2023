# HTTP GETリクエストを使用して競技サーバーにアクセスする。
# リクエストとは、他方へ送信する要求メッセージなどのこと
import requests
import json
import logging
import keyboard
import time


# -------- logの設定 --------
logger = logging.getLogger('Log')
log_lebel = 10
logger.setLevel(log_lebel)
#logをコンソール出力するための設定
sh = logging.StreamHandler()
logger.addHandler(sh)
#logのファイル出力先設定
log_file_path = "./logs.log"
fh = logging.FileHandler(log_file_path)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s --- message : %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

server_url = "http//localhost:3000"# サーバーのURL
token_file = "C:/Users/kxiyt/Desktop/token.txt"
with open(token_file, encoding="UTF-8") as f:
    f_text = f.read()
token_text = f_text
token_text = "abc12345" # テスト用




# 初期状態の情報を取得 (デフォルトではサーバーを起動して10秒以内にアクセス)
def initial_requests():
    try:
        # サーバーから試合状態を取得
        response = requests.get(f"http://localhost:3000/matches?token={token_text}") # テスト用（初期状態を取得）
        if response.status_code == 200 or response.status_code == 201 or response.status_code == 404: # 正常なstatus_codeは[200]
            field_data = response.json()
            print(f"試合の初期状態を取得しました。（status_code : {response.status_code}）")
            print(field_data)
        else:
            print(f"エラーが発生しました。（status_code : {response.status_code}）")
    except requests.exceptions.RequestException as e:
        print("HTTPリクエストエラー:", e)
        
    if field_data:
        logger.log(100, "Match has started, Get initial states")
        
        # -------- 試合情報の取得 --------
        match_id = field_data['matches'][0]['id'] # 試合のID
        turns_num = field_data['matches'][0]['turns'] # 総ターン数
        turns_seconds = field_data['matches'][0]['turnSeconds'] # １ターンの制限時間
        # 各ボーナスポイント
        wall_point = field_data['matches'][0]['bonus']['wall'] # 城壁のボーナスポイント
        territory_point = field_data['matches'][0]['bonus']['territory'] # 陣地のボーナスポイント
        castle_point = field_data['matches'][0]['bonus']['castle'] # 城のボーナスポイント
        masons_num = field_data['matches'][0]['board']['mason'] # 職人の数
        board_size = [field_data['matches'][0]['board']['width'], field_data['matches'][0]['board']['height']] # フィールドのサイズ（縦x横）
        board_weight = board_size[0]
        #print(f"試合ID : {match_id},  総ターン数 : {turns_num},  1ターン制限時間 : {turns_seconds},  職人の数 : {masons_num},  フィールドの幅 : {board_weight}")
        logger.log(100, f"match_id : {match_id},  turns_num : {turns_num},  turns_seconds : {turns_seconds},  masons_num : {masons_num},  board_weight : {board_weight}")

        # フィールド情報｛二次元配列（縦x横）｝
        structures = field_data['matches'][0]['board']['structures'] # 構造物（0：無配置, 1：池, 2：城）
        masons = field_data['matches'][0]['board']['masons'] # 職人（正：自チーム, 負：相手チーム, 数字の絶対値が小さい順に行動）
        arr_structures = []
        for row in structures:
            arr_structures.append(row)
        arr_masons = []
        for row in masons:
            arr_masons.append(row)
        structures = [[30 if cell == 1 else cell for cell in row] for row in structures]
        structures = [[400 if cell == 2 else cell for cell in row] for row in structures]
        temp_array = [[0 for _ in range(board_size[0])] for _ in range(board_size[0])]
        a = [structures, temp_array, temp_array] # ２次元配列を3次元配列にする
        
    else:
        print("no initial field_data")
        
    # 戻り値 : 試合id, 総ターン数, １ターン制限時間, 職人の数, フィールドの幅, 構造物, 職人
    returns = [match_id, turns_num, turns_seconds, masons_num, board_weight, arr_structures, arr_masons]
    return returns

    
    
# 毎ターンごとの状態取得
def turns_requests(matches_id):
    try:
        # サーバーから試合状態を取得
        #response = requests.get(f"{server_url}/matches/10?token={token_text}")
        response = requests.get(f"http://localhost:3000/matches/{matches_id}?token={token_text}") # テスト（1ターン目以降の情報を取得）
        if response.status_code == 200 or response.status_code == 201 or response.status_code == 404: # 正常なstatus_codeは[200]
            field_data = response.json()
            print(f"試合の状態を取得しました。（status_code : {response.status_code}）")
            #print(field_data)
        else:
            print(f"エラーが発生しました。（status_code : {response.status_code}）")
    except requests.exceptions.RequestException as e:
        print("HTTPリクエストエラー:", e)
        
    if field_data:
        # -------- 試合情報の取得 --------
        match_id = field_data['id'] # 試合のID
        turns_num = field_data['turn'] # 現在のターン数
        masons_num = field_data['board']['mason'] # 職人の数
        board_size = [field_data['board']['width'], field_data['board']['height']] # フィールドのサイズ（縦x横）
        board_weight = board_size[0]
        #print(f"試合ID : {match_id},  現在のターン数 : {turns_num})
        logger.log(100, f"match_id : {match_id},  turns_num : {turns_num}")

        # フィールド情報｛二次元配列（縦x横）｝
        structures = field_data['board']['structures'] # 構造物（0：無配置, 1：池, 2：城）
        masons = field_data['board']['masons'] # 職人（正：自チーム, 負：相手チーム, 数字の絶対値が小さい順に行動）
        walls = field_data['board']['walls'] # 城壁（0：なし, 1：自チーム, 2：相手チーム）
        territories = field_data['board']['walls'] # 陣地（0：中立, 1：自チーム, 2：相手チーム）
        arr_structures = []
        for row in structures:
            arr_structures.append(row)
        arr_masons = []
        for row in masons:
            arr_masons.append(row)
        arr_walls = []
        for row in walls:
            arr_walls.append(row)    
        arr_territories = []
        for row in territories:
            arr_territories.append(row)    
            
        structures = [[30 if cell == 1 else cell for cell in row] for row in structures]
        structures = [[400 if cell == 2 else cell for cell in row] for row in structures]
        
    else:
        print("no field_data")

    # logsをlogs.logに保存する
    logs_txt = field_data['logs']
    logger.log(100, f"{logs_txt}")
    
    # 戻り値 : 試合id, ターン数, 構造物, 職人, 城壁, 陣地
    returns = [match_id, turns_num, arr_structures, arr_masons, arr_walls, arr_territories]
    return returns


# 行動計画更新
def send_requests(matches_id):
    pass




# def on_key_event(e):
#     if e.name() == "w":
#         print("「w」キーが押されたので試合を開始します。")
# keyboard.hook(on_key_event)

a = initial_requests()
if a:
    # 時間カウントをスタートする
    time_sta = time.time()
# 初期状態の返り値を各変数に代入
match_id = a[0] # 試合id
turns_num = a[1] # ターン数
turns_seconds = a[2] # １ターンの制限時間
masons_num = a[3] # 職人の数
board_weight = a[4] # フィールドの幅
arr_structures = a[5] # 城壁の初期状態 (2次元配列)
arr_masons = a[6] # 陣地の初期状態 (2次元配列)

# 初期状態を取得してから一定の時間が経過したら１ターン目の情報の取得を開始
while True:
    time_end = time.time()
    if time_end - time_sta >= 9:
        break
    
# ３秒ごとに
count_turns_tmp = turns_num
while count_turns_tmp > 0:
    b = turns_requests(match_id)
    count_turns_tmp -= 1
    time.sleep(3)
    
print("終わりました。")
    
# c = send_requests(matches_id)