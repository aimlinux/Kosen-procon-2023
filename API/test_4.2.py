import json



json_file = "./2_turn.json"
with  open(f"{json_file}", encoding='UTF-8', mode='r') as json_file:
    data = json.load(json_file)

# 1ターン目以降のjsonファイルを読み込んだ時
match_id = data['id'] 
turn = data['id']['turn'] # 現在のターン数
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
    
# 0がコマ数, １が横, ２が縦
    
# 池３０　城４００　城壁1000000 
    
structures = [[30 if cell == 1 else cell for cell in row] for row in structures]

print(structures)