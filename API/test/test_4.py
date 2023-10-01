import json 

with  open("./setting.json", encoding='UTF-8', mode='r') as json_file:
    data = json.load(json_file)
    
# -------- 試合情報の取得 --------
match_id = data['match']['id'] # 試合のID
turns_num = data['match']['turns'] # ターン数
turns_seconds = data['match']['turnSeconds'] # １ターンの制限時間
# 各ボーナスポイント
# wall_point = data['match']['bonus']['wall'] # 城壁のボーナスポイント
# territory_point = data['match']['bonus']['castle'] # 陣地のボーナスポイント
# castle_point = data['match']['bonus']['castle'] # 城のボーナスポイント
# print(match_id, turns_num, turns_seconds, wall_point, territory_point, castle_point)



masons_num = data['match']['board']['mason'] # 職人の数
board_size = [data['match']['board']['width'], data['match']['board']['height']] # フィールドのサイズ（縦x横）
print(match_id, masons_num, board_size)

# フィールド情報｛二次元配列（縦x横）｝
structures = data['match']['board']['structures'] # 構造物（0：無配置, 1：池, 2：城）
masons = data['match']['board']['masons'] # 職人（正：自チーム, 負：相手チーム, 数字の絶対値が小さい順に行動）

arr_structures = []
for row in structures:
    arr_structures.append(row)
arr_masons = []
for row in masons:
    arr_masons.append(row)

    