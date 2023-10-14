import tkinter as tk


def AppGUI(arg):
    
    structures = arg[0]
    masons = arg[1]
    walls = arg[2]
    territories = arg[3]
    board_weight:int = arg[4]
    print(board_weight)
    
    # print(structures)
    # print("\n\n\n")
    # print(masons)
    
    root = tk.Tk()
    root.title("GUI")
    root.geometry(f"1080x720+100+100")
    root.lift()
    
    pw_main = tk.PanedWindow(root, bg="#fff", orient="vertical")
    pw_main.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
    fm_main = tk.Frame(pw_main, bd=5, bg="#fffff2", relief="ridge", borderwidth=10)
    pw_main.add(fm_main)
    
    fm_fields_lower = tk.Frame(fm_main, bd=5, bg="#e6e6fa", relief="ridge", borderwidth=10)
    fm_fields_lower.pack(side=tk.LEFT, padx=(20, 20), pady=(20, 20))
    fm_fields = tk.Frame(fm_fields_lower, bg="#e6e6fa")
    fm_fields.pack(padx=(10, 10), pady=(10, 10))
    fm_event = tk.Frame(fm_main, bd=5, bg="#e6e6fa", relief="groove", borderwidth=10)
    fm_event.pack(side=tk.RIGHT, padx=(20, 20), pady=(20, 20))
    
    
    # 1irohaの大きさを設定
    if board_weight == 25:  iroha_weight = 17
    elif board_weight >= 21:  iroha_weight = 19
    elif board_weight >= 17:  iroha_weight = 25
    elif board_weight >= 15:  iroha_weight = 30
    elif board_weight >= 13:  iroha_weight = 33
    elif board_weight >= 11:  iroha_weight = 38
        
    # irohaの背景を設定
    # iroha_bg_list = [0]*board_weight[0]*board_weight
    iroha_bg_list = [[0 for _ in range(board_weight)] for _ in range(board_weight)] # 毎ターン二次元配列を0で初期化
    
    for i in range(0, board_weight) :
        for j in range(0, board_weight):
            #print(structures[i][j])
            # ---- arr_structuresについて ----
            if structures[i][j] == 1: # 池
                iroha_bg_list[i][j] = "#111111"
            elif structures[i][j] == 2: # 城
                iroha_bg_list[i][j] = "#ffff00"
            elif structures[i][j] == 0: # 無所属
                iroha_bg_list[i][j] = "#fff" 
            
            # ---- arr_masonsについて ----
            if masons[i][j] > 0: # 先攻の職人
                if iroha_bg_list[i][j] == "#fff":
                    if masons[i][j] == 1: iroha_bg_list[i][j] = "#ff0000" # 赤色
                    elif masons[i][j] == 2: iroha_bg_list[i][j] = "#ff8080"
                    elif masons[i][j] == 3: iroha_bg_list[i][j] = "#ffb3b3"
                    elif masons[i][j] == 4: iroha_bg_list[i][j] = "#e6cfcf"
            elif masons[i][j] < 0: # 後攻の職人
                if iroha_bg_list[i][j] == "#fff":
                    if masons[i][j] == -1: iroha_bg_list[i][j] = "#0000ff" # 青色
                    elif masons[i][j] == -2: iroha_bg_list[i][j] = "#6666ff"
                    elif masons[i][j] == -3: iroha_bg_list[i][j] = "#9999ff"
                    elif masons[i][j] == -4: iroha_bg_list[i][j] = "#ccccff"
            
            # ---- arr_wallsについて ----
            # if not walls == None:
            #     if 
            
    # for i in range(0, board_weight):
    #     for i in range(0, board_weight):
    #         if iroha_bg_list[i][j] == 0:
    #             iroha_bg_list[i][j] = "#fff" # 何も構造物がないマスは白色で初期化
                

        
                
            
    
    # -------- 二次元配列でフィールドを表示
    for i in range(0, board_weight):
        for j in range(0, board_weight):
            hon = tk.Frame(fm_fields, bd=2, bg=iroha_bg_list[i][j], height=iroha_weight, width=iroha_weight+10)
            hon.grid(column=i, row=j, padx=7, pady=7)
        
        
    root.after(3000, root.destroy)
        
    root.mainloop()
    
    


arr_structures_test = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        [ 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0],
        [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [ 0, 1, 0, 0, 2, 0, 2, 0, 0, 1, 0],
        [ 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [ 0, 1, 0, 0, 2, 0, 2, 0, 0, 1, 0],
        [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [ 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0],
        [ 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
arr_masons_test = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0,-1, 0, 0, 0, 0, 0, 0, 0,-2, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

arg = [arr_structures_test, arr_masons_test, None, None, 11]
AppGUI(arg)