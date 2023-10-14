# HTTP GET & POSTリクエストを使用して競技サーバーにアクセスする。

import requests
import json
import logging
import time
#import gui


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

# server_url = "http//localhost:3000"# サーバーのURL
# token_file = "C:/Users/kxiyt/Desktop/token.txt"
# with open(token_file, encoding="UTF-8") as f:
#     f_text = f.read()
# token_text = f_text
token_text = "abc12345" # テスト用



# 初期状態の情報を取得 (デフォルトではサーバーを起動して10秒以内にアクセス)
def initial_requests():
    field_data = None # 初期化
    match_id = 0  # 初期化
    turns_num = 0  # 初期化
    turns_seconds = 0  # 初期化
    masons_num = 0  # 初期化
    board_size = 0 # 初期化
    board_weight = 0  # 初期化
    arr_structures = []  # 初期化
    arr_masons = []  # 初期化
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
    field_data = None # 初期化
    try:
        # サーバーから試合状態を取得
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
def send_requests(matches_id, turns, masons, type_arr, dir_arr):
    # ヘッダーを設定
    headers = {
        "Content-Type": "application/json",
        "procon-token": token_text
    }
    # クエリパラメータを設定
    query_params = {
        "token" : token_text
    }
    turn = turns # 更新するターン数
    match_id = matches_id # 試合ID
    # 職人の数だけactionsの配列を用意する
    actions_arr = []
    masons_tmp = masons

    for i in range(0, masons_tmp):
        tmp = {
            "type": type_arr[i],
            "dir": dir_arr[i],
        }
        actions_arr.append(tmp)
    
    # リクエストボディを作成
    request_body = {
        "turn": turn, 
        "actions": actions_arr
    }
    
    url = f"http://localhost:3000/matches/{match_id}" # テスト用
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
            return 10
    except requests.exceptions.RequestException as e:
        print("HTTPリクエストエラー:", e)
        return 10
    
    return 0
    
    


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

arg = [arr_structures, arr_masons, None, None, board_weight]
# ---------------- 初期状態をGUIに反映 ----------------
# if arg:
#     gui.AppGUI(arg)

# 初期状態を取得してから一定の時間が経過したら１ターン目の情報の取得を開始
while True:
    time_end = time.time()
    if time_end - time_sta >= 9:
        break
    
# １ターンの制限時間ごとに
count_turns_tmp = turns_num
turn_count = 1
while count_turns_tmp > 0:
    if turn_count % 2 == 0:
        print("相手のターン\n")
    else:
        x_time = time.time()
        b = turns_requests(match_id)
        arg = [b[2], b[3], b[4], b[5], None]
        print(b[4])
        print("\n\n")
        print(b[5])
# ---------------- GUIを更新する ----------------
        #gui.AppGUI(arg)
        
        count_turns_tmp -= 1
        
        # ---- 行動計画更新 ----
        turns = turn_count # 更新するターン数を決める
        masons = masons_num
        type_arr = [0]*masons_num # 職人の総数の行動を配列に入れる
        dir_arr = [0]*masons_num # 職人の総数の方向を配列に入れる
        type_arr = [2, 2]
        dir_arr = [4, 2]
        # "行動タイプです。\\\n0: 滞在, 1: 移動, 2: 建築, 3: 解体",
        # "競技ボードの左上を (1,1) とする座標系における方向です。\\\n0: 無方向, 1: 左上, 2: 上, 3: 右上, 4: 右, 5: 右下, 6: 下, 7: 左下, 8: 左",
        # リクエストを送る
        c = send_requests(match_id, turns, masons, type_arr, dir_arr)
        if c == 10:
            print("-------- Requests Error --------\n\n")
        elif c == 0:
            print("-------- Requests Complete --------\n\n")
    
    turn_count += 1
    time.sleep(turns_seconds-0.01)
    
print("終わりました。")
    
