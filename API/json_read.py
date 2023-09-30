import json

initial_turn = True

# 初期状態を取得する時
if initial_turn:
    json_file = "./setting.json"
    with open(f"{json_file}", encoding='UTF-8', mode="r") as json_file:
        initial_data = json.load(json_file)


    # 初期状態のjsonファイルを読み込んだ時
    # -------- 試合情報の取得 --------
    match_id = initial_data['match']['id'] # 試合のID
    turns_num = initial_data['match']['turns'] # ターン数
    turns_seconds = initial_data['match']['turnSeconds'] # １ターンの制限時間
    # 各ボーナスポイント
    # wall_point = initial_data['match']['bonus']['wall'] # 城壁のボーナスポイント
    # territory_point = initial_data['match']['bonus']['castle'] # 陣地のボーナスポイント
    # castle_point = initial_data['match']['bonus']['castle'] # 城のボーナスポイント
    # print(match_id, turns_num, turns_seconds, wall_point, territory_point, castle_point)

    masons_num = initial_data['match']['board']['mason'] # 職人の数
    board_size = [initial_data['match']['board']['width'], initial_data['match']['board']['height']] # フィールドのサイズ（縦x横）

    # フィールド情報｛二次元配列（縦x横）｝
    structures = initial_data['match']['board']['structures'] # 構造物（0：無配置, 1：池, 2：城）
    masons = initial_data['match']['board']['masons'] # 職人（正：自チーム, 負：相手チーム, 数字の絶対値が小さい順に行動）

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
    
# １ターン目以降の情報を取得する時
else:
    json_file = "./2_turn.json"
    with  open(f"{json_file}", encoding='UTF-8', mode='r') as json_file:
        data = json.load(json_file)

    # 1ターン目以降のjsonファイルを読み込んだ時
    match_id = data['id'] 
    turn = data['turn'] # 現在のターン数
    board_size = [data['board']['width'], data['board']['height']]
    masons_num = data['board']['mason']

    # フィールド情報｛二次元配列（縦x横）｝
    structures = data['board']['structures'] # 構造物（0：無配置, 1：池, 2：城）
    masons = data['board']['masons'] # 職人（正：自チーム, 負：相手チーム, 数字の絶対値が小さい順に行動）
    walls = data['board']['walls'] # 城壁（0：なし, 1：自チーム, 2：相手チーム）
    territories = data['board']['walls'] # 陣地（0：中立, 1：自チーム, 2：相手チーム）
            
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
    temp_array = [[0 for _ in range(board_size[0])] for _ in range(board_size[0])]
    a = [structures, temp_array, temp_array] # ２次元配列を3次元配列にする
