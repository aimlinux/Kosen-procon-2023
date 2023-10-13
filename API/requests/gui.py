import tkinter as tk


def AppGUI(arg):
    
    structures = arg[0]
    masons = arg[1]
    walls = arg[2]
    territories = arg[3]
    board_weight:int = arg[4]
    print(board_weight)
    
    root = tk.Tk()
    

    root.title("GUI")
    root.geometry(f"1080x720+100+100")
    root.lift()
    
    pw_main = tk.PanedWindow(root, bg="#fff", orient="vertical")
    pw_main.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
    fm_main = tk.Frame(pw_main, bd=5, bg="#fffff2", relief="ridge", borderwidth=10)
    pw_main.add(fm_main)
    
    fm_fields = tk.Frame(fm_main, bd=5, bg="#ffffff", relief="groove", borderwidth=10)
    fm_fields.pack(side=tk.LEFT, padx=(20, 20), pady=(20, 20))
    
    fm_event = tk.Frame(fm_main, bd=5, bg="#fffeee", relief="groove", borderwidth=10)
    fm_event.pack(side=tk.RIGHT, padx=(20, 20), pady=(20, 20))
    
    
    
    hon = tk.Frame(fm_fields, bd=2, bg="lightblue", height=10, width=10, padx=10, pady=10)
    hon.grid(column=0, row=1)
    

    # 一列目
    for i in range(0, board_weight):
        for j in range(0, board_weight):
            hon = tk.Frame(fm_fields, bd=2, bg="lightblue", height=20, width=20)
            hon.grid(column=i, row=j, padx=5, pady=5)
        
    #     space_label = tk.Label(fm_fields, text="", bg="red", height=5, width=1000)
    #     space_label.pack(side=tk.TOP, expand=True)
        
        
    # for i in (0, board_weight):
    #     hon = tk.Frame(fm_fields, bd=2, bg="lightblue", height=10, width=10)
    #     hon.pack(side=tk.LEFT, padx=(2, 2), pady=(2, 2))
    
    # space_label = tk.Label(fm_fields, text="", bg="red", height=5, width=1000)
    # space_label.pack(side=tk.TOP, expand=True)
    
    
    root.mainloop()
    
    
arg = [None, None, None, None, 18]
AppGUI(arg)