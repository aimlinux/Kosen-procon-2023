import tkinter as tk
import random as rnd
import numpy as np
import sys

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("A11")
        self.root.resizable(False, False)  # ウィンドウサイズ変更無効

        # ゲームの初期設定をここで行う
        self.initialize_game()

        # キャンバスの作成
        self.create_canvas()

        # ボタンの作成
        self.create_buttons()

        # イベントの設定
        self.root.bind("<Button>", self.click)

    def initialize_game(self):
        # ゲームの初期設定をここで行う
        self.p = 0
        self.takumi = 0
        self.kodojun = [0, 3, 2, 1]
        
        # 他の初期化処理をここに追加

    def create_canvas(self):
        # キャンバスの作成と初期設定
        self.h_width = 28
        self.w_width = 40
        self.w_h = (self.w_width - self.h_width) / 2
        self.color = ["red", "blue", "green"]
        self.tilal = ["#ffaaaa", "#aaaaff"]  # 城壁の色
        self.jin = ["#ffe4e1", "#e0ffff"]

        self.N = 61 / 293
        self.M = 15 - 7381 / 1758
        self.h = 11  # 縦マス
        self.w = 11  # 横マス
        self.shoku = 4  # 職人の数
        self.act = [0] * self.shoku
        self.bec = [0] * self.shoku
        self.jid = [[], []]
        self.jon = [0, 0]
        self.turn = rnd.randint(int(self.h * self.w / self.shoku * self.N + self.M),
                                int(self.h * self.w / self.shoku * self.N + self.M + 25)) * 2
        self.ike = 24  # 池の数
        self.siro = 9  # 城の数
        
        # 職人=10,20+a  池=30  城=400  城壁=100000,200000
        self.a = [[[0 for i in range(self.w)] for j in range(self.h)] for k in range(3)]  # ３次元配列でゲームボードの状態を表現
        self.sh = [[[0 for i in range(2)] for j in range(self.shoku)]
                    for k in range(2)]  # [[0,0]*shoku,[0,0]*shoku]

        # 職人aを配置
        sh0_x = [1, 1, 9, 9]  # 駒の配置は左上から右下の順番で
        sh0_y = [1, 9, 1, 9]
        i = 0
        while i < self.shoku:
            x = sh0_x[i]
            y = sh0_y[i]
            if self.a[0][y][x] == 0:
                self.a[0][y][x] = 10 + i
                self.sh[0][i][0] = x
                self.sh[0][i][1] = y
                i += 1

        # 職人bを配置
        sh1_x = [2, 5, 5, 8]
        sh1_y = [5, 2, 8, 5]
        i = 0
        while i < self.shoku:
            x = sh1_x[i]
            y = sh1_y[i]
            if self.a[0][y][x] == 0:
                self.a[0][y][x] = 20 + i
                self.sh[1][i][0] = x
                self.sh[1][i][1] = y
                i += 1

        # 池を配置
        ike_x = [0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10]
        ike_y = [5, 4, 6, 4, 6, 3, 7, 1, 2, 8, 9, 0, 10, 1, 2, 8, 9, 3, 7, 4, 6, 4, 6, 5]
        i = 0
        self.ik = [[0, 0]] * self.ike
        while i < self.ike:
            x = ike_x[i]
            y = ike_y[i]
            if self.a[0][y][x] == 0:
                self.a[0][y][x] = 30
                self.ik[i][0] = x
                self.ik[i][1] = y
                i += 1

        # 城を配置
        si_x = [2, 2, 4, 4, 5, 6, 6, 8, 8]
        si_y = [2, 8, 4, 6, 5, 4, 6, 2, 8]
        i = 0
        self.si = [[0, 0]] * self.siro
        while i < self.siro:
            x = si_x[i]
            y = si_y[i]
            if self.a[0][y][x] == 0:
                self.a[0][y][x] = 400
                self.si[i][0] = x
                self.si[i][1] = y
                i += 1
                
                


        # self.root = tk.Tk()
        # self.root.title("A11")
        # self.root.resizable(False, False) # vウィンドウサイズ変更無効
        self.cvs = tk.Canvas(width=self.w_width*self.w+500, heigh=self.h_width*self.h+30, bg="white")
        # cvs.create_text(800,300,text="三目並べDX",fill="navy",font=("Times New Roman",60))
        # 縦のグリッド線を描画
        for i in range(self.h+1):
            self.cvs.create_line(10, 10+self.h_width*i, 10+self.w_width*self.w,
                            10+self.h_width*i, fill="black", width=3)
        # 横のグリッド線を描画
        for i in range(self.w+1):
            self.cvs.create_line(10+self.w_width*i, 10, 10+self.w_width*i,
                            10+self.h_width*self.h, fill="black", width=3)

        id = [[0]*self.shoku, [0]*self.shoku] # 4 (職人の数) * 2 の二次元配列作成

        for i in range(self.h):
            for j in range(self.w):
                if self.a[0][i][j]//10 == 3:
                    self.cvs.create_rectangle(21+j*self.w_width, 17+i*self.h_width, (j+1)
                                        * self.w_width, 4+(i+1)*self.h_width, fill="black", width=0)
                if self.a[0][i][j]//100 == 4:
                    self.cvs.create_rectangle(12+j*self.w_width, 12+i*self.h_width, 9+(j+1) *
                                        self.w_width, 9+(i+1)*self.h_width, fill="yellow", width=0, tag="400")
                if self.a[0][i][j] % 100//10 == 1:
                    id[0][self.a[0][i][j] % 10] = self.cvs.create_oval(13+j*self.w_width+self.w_h, 13+i*self.h_width, 7+(
                        j+1)*self.w_width-self.w_h, 7+(i+1)*self.h_width, fill=self.color[0], width=0, tag="s1")
                if self.a[0][i][j] % 100//10 == 2:
                    id[1][self.a[0][i][j] % 10] = self.cvs.create_oval(13+j*self.w_width+self.w_h, 13+i*self.h_width, 7+(
                        j+1)*self.w_width-self.w_h, 7+(i+1)*self.h_width, fill=self.color[1], width=0, tag="s2")
        self.cvs.itemconfig(id[0][0], fill=self.color[2])
        self.cvs.lift("s1")
        self.cvs.lift("s2")
        # cvs.lower("400")
        # fg=cvs.create_rectangle(0,0,500,500,fill="#aaaaff")
        # cvs.lower(fg)
                
                

    def create_buttons(self):
        # ボタンの作成と初期設定
        rightt = 10 + self.w_width * self.w
        wspace = 30
        hspace = 30
        www = 110
        hhh = 70

        self.bu = [0] * 4
        self.but = [0] * 9
        self.bu[0] = tk.Button(self.root, text="滞在", bg="red", command=lambda: self.action(0))
        self.bu[0].place(x=rightt + wspace, y=hspace, width=www, height=hhh)
        self.bu[1] = tk.Button(self.root, text="移動", bg="white", command=lambda: self.action(1))
        self.bu[1].place(x=rightt + wspace, y=hspace + hhh, width=www, height=hhh)
        self.bu[2] = tk.Button(self.root, text="建築", bg="white", command=lambda: self.action(2))
        self.bu[2].place(x=rightt + wspace, y=hspace + hhh * 2, width=www, height=hhh)
        self.bu[3] = tk.Button(self.root, text="解体", bg="white", command=lambda: self.action(3))
        self.bu[3].place(x=rightt + wspace, y=hspace + hhh * 3, width=www, height=hhh)
        self.but[0] = tk.Button(self.root, text='↖', bg='gray', command=lambda: self.bector(0))
        self.but[0].place(x=rightt + wspace * 2 + www, y=hspace, width=www, height=hhh)
        self.but[1] = tk.Button(self.root, text='↑', bg='white', command=lambda: self.bector(1))
        self.but[1].place(x=rightt + wspace * 2 + www * 2, y=hspace, width=www, height=hhh)
        self.but[2] = tk.Button(self.root, text='↗', bg='white', command=lambda: self.bector(2))
        self.but[2].place(x=rightt + wspace * 2 + www * 3, y=hspace, width=www, height=hhh)
        self.but[3] = tk.Button(self.root, text='←', bg='white', command=lambda: self.bector(3))
        self.but[3].place(x=rightt + wspace * 2 + www, y=hspace + hhh, width=www, height=hhh)
        self.but[5] = tk.Button(self.root, text='→', bg='white', command=lambda: self.bector(5))
        self.but[5].place(x=rightt + wspace * 2 + www * 3, y=hspace + hhh, width=www, height=hhh)
        self.but[6] = tk.Button(self.root, text='↙', bg='white', command=lambda: self.bector(6))
        self.but[6].place(x=rightt + wspace * 2 + www, y=hspace + hhh * 2, width=www, height=hhh)
        self.but[7] = tk.Button(self.root, text='↓', bg='white', command=lambda: self.bector(7))
        self.but[7].place(x=rightt + wspace * 2 + www * 2, y=hspace + hhh * 2, width=www, height=hhh)
        self.but[8] = tk.Button(self.root, text='↘', bg='white', command=lambda: self.bector(8))
        self.but[8].place(x=rightt + wspace * 2 + www * 3, y=hspace + hhh * 2, width=www, height=hhh)
        self.enter = tk.Button(self.root, text='確定', bg='gray', command=self.submit)
        self.enter.place(x=rightt + wspace * 2 + www * 2, y=hspace + hhh, width=www, height=hhh)
        self.txt = self.cvs.create_text(rightt + wspace * 2 + www * 2.5, hspace + hhh * 3.5, text="残りターン数 " + str(self.turn), font=("", 24))

    def action(self, n):
        # action 関数のコードをここに移動
        pass

    def bector(self, n):
        # bector 関数のコードをここに移動
        pass

    def submit(self):
        # submit 関数のコードをここに移動
        pass

    def click(self, e):
        # click 関数のコードをここに移動
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()