import tkinter as tk
import random as rnd
import numpy as np
import sys


def action(n):
    global act, color, p, takumi
    if act[takumi] != n:
        bu[act[takumi]].config(bg="white")
        act[takumi] = n
        bu[n].config(bg=color[p])
        if act[takumi] == 0:
            but[bec[takumi]].config(bg="gray")
        elif act[takumi] > 1 and bec[takumi] % 2 == 0:
            but[bec[takumi]].config(bg="gray")
        else:
            but[bec[takumi]].config(bg=color[p])


def bector(n):
    global bec, act, color, p, takumi
    if bec[takumi] != n:
        but[bec[takumi]].config(bg="white")
        bec[takumi] = n
        if act[takumi] == 0:
            but[n].config(bg="gray")
        elif act[takumi] > 1 and n % 2 == 0:
            but[n].config(bg="gray")
        else:
            but[n].config(bg=color[p])


def submit():
    global bec, act, color, p, takumi, turn, w, h, sh, h_width, w_width
    cvs.itemconfig("s"+str(p+1), fill=color[p])
    bu[act[takumi]].config(bg="white")
    but[bec[takumi]].config(bg="white")
    for j in kodojun:
        for i in range(shoku):
            shx = sh[p][i][0]
            shy = sh[p][i][1]
            ax = shx+bec[i] % 3-1
            ay = shy+bec[i]//3-1
            if act[i] == 0:  # 滞在
                pass
            elif act[i] == j and j == 1:  # 移動
                if ax >= 0 and ax < w and ay >= 0 and ay < h:
                    if a[0][ay][ax] == 0 or a[0][ay][ax] == 400 or a[0][ay][ax] == (p+1)*100000:
                        sh[p][i][0] = ax
                        sh[p][i][1] = ay
                        # cvs.lift(id[p][i])
                        a[0][ay][ax] += (p+1)*10+i
                        a[0][shy][shx] -= (p+1)*10+i
                        cvs.move(id[p][i], (bec[i] % 3-1) *
                                 w_width, (bec[i]//3-1) * h_width)
            elif act[i] == j and j == 2:  # 建築
                if ax >= 0 and ax < w and ay >= 0 and ay < h and bec[i] % 2 == 1:
                    n = a[0][ay][ax]
                    if n//100 == 0 and n/10 % 10 != 2-p:
                        a[0][ay][ax] += (p+1) * 100000+jon[p]*100
                        jon[p] += 1
                        a[p+1][ay][ax] = jon[p]*10
                        jid[p] = jid[p] + [cvs.create_rectangle(12+ax*w_width, 12+ay*h_width,9+(
                            ax+1)*w_width,9+(ay+1)*h_width, fill=tilal[p], width=0)]
                        
            elif act[i]==j and j == 3:  # 解体
                if ax >= 0 and ax < w and ay >= 0 and ay < h and bec[i] % 2 == 1:
                    n = a[0][ay][ax]
                    #print(jid[p][ n//100 % 1000])
                    if n//100000 != 0:
                        a[0][ay][ax] = n % 100
                        #print(jid[p][ n//100 % 1000])
                        cvs.delete(jid[n//100000-1][ n//100 % 1000])
                        a[n//100000][ay][ax] = 0
    aa = np.array(a[p+1])
    for i in range(np.shape(a)[1]):
        if aa[i][0] == 0:
            aa[i][0] = -1
        if aa[i][-1] == 0:
            aa[i][-1] = -1
    for j in range(np.shape(a)[2]):
        if aa[0][j] == 0:
            aa[0][j] = -1
        if aa[-1][j] == 0:
            aa[-1][j] = -1
    print(aa)
    # jinti(p,a,0,1,aa,np.zeros_like(aa),1,1)      
    if turn == 1:
        sys.exit()
    p = 1-p
    turn -= 1
    takumi = 0
    act = [0]*shoku
    bec = [0]*shoku
    cvs.itemconfig(txt, text="残りターン数  "+str(turn))
    cvs.itemconfig(id[p][takumi], fill=color[2])
    bu[0].config(bg=color[p])
    but[0].config(bg="gray")



def click(e):
    global h_width, w_width, h, w, p, color, takumi
    if e.x < w_width*w+10 and e.y < h_width*h+10 and e.x >= 10 and e.y >= 10:
        cx = (e.x-10)//w_width
        cy = (e.y-10)//h_width
        if a[0][cy][cx] % 100//10 == p+1:
            n = a[0][cy][cx] % 10
            cvs.itemconfig("s"+str(p+1), fill=color[p])
            cvs.itemconfig(id[p][n], fill=color[2])
            bu[act[takumi]].config(bg="white")
            but[bec[takumi]].config(bg="white")
            takumi = n
            bu[act[n]].config(bg=color[p])
            if act[takumi] == 0:
                but[bec[takumi]].config(bg="gray")
            elif act[takumi] > 1 and bec[takumi] % 2 == 0:
                but[bec[takumi]].config(bg="gray")
            else:
                but[bec[takumi]].config(bg=color[p])


p = 0
takumi = 0
kodojun = [0, 3, 2, 1]

h_width = 28
w_width = 40
w_h = (w_width-h_width)/2
color = ["red", "blue", "green"]
tilal = ["#ffaaaa", "#aaaaff"]  # 城壁の色
jin = ["#ffe4e1","#e0ffff"] 

N = 61/293
M = 15-7381/1758
h = 15 # 縦マス  
w = 15 # 横マス  
shoku = 4 # 職人の数
act = [0]*shoku
bec = [0]*shoku
jid = [[],[]]
jon = [0, 0]
turn = rnd.randint(int(h*w/shoku*N+M), int(h*w/shoku*N+M+25))*2
ike = 45 #池の数
siro =20 #城の数

# 職人=10,20+a  池=30  城=400  城壁=100000,200000
a = [[[0 for i in range(w)] for j in range(h)] for k in range(3)] # ３次元配列でゲームボードの状態を表現
sh = [[[0 for i in range(2)] for j in range(shoku)]
    for k in range(2)]  # [[0,0]*shoku,[0,0]*shoku]

# 職人aを配置
sh0_x = [5,7,7,9] #駒の配置は左上から右下の順番で
sh0_y = [7,1,13,7]
i = 0
while i < shoku:
    x = sh0_x[i]
    y = sh0_y[i]
    if a[0][y][x] == 0:
        a[0][y][x] = 10+i
        sh[0][i][0] = x
        sh[0][i][1] = y
        i += 1
# 職人bを配置
sh1_x = [1,7,7,13]
sh1_y = [7,5,9,7]
i = 0
while i < shoku:
    x = sh1_x[i]
    y = sh1_y[i]
    if a[0][y][x] == 0:
        a[0][y][x] = 20+i
        sh[1][i][0] = x
        sh[1][i][1] = y
        i += 1
# 池を配置
ike_x = [1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5,6,6,7,7,7,7,7,8,8,9,9,10,10,10,11,11,11,11,12,12,12,12,12,13,13,13,13]
ike_y = [2,6,8,12,1,2,7,12,13,3,4,10,11,3,7,11,5,9,1,13,2,4,7,10,12,1,13,5,9,3,7,11,3,4,10,11,1,2,7,12,13,2,6,8,12]
i = 0
ik = [[0, 0]]*ike
while i < ike:
    x = ike_x[i]
    y = ike_y[i]
    if a[0][y][x] == 0:
        a[0][y][x] = 30
        ik[i][0] = x
        ik[i][1] = y
        i += 1
# 城を配置
si_x = [1,1,2,2,4,4,5,5,6,6,8,8,9,9,10,10,12,12,13,13]
si_y = [1,13,5,9,4,10,2,12,6,8,6,8,2,12,4,10,5,9,1,13]
i = 0
si = [[0, 0]]*siro
while i < siro:
    x = si_x[i]
    y = si_y[i]
    if a[0][y][x] == 0:
        a[0][y][x] = 400
        si[i][0] = x
        si[i][1] = y
        i += 1


root = tk.Tk()
root.title("B15")
root.resizable(False, False) # vウィンドウサイズ変更無効
cvs = tk.Canvas(width=w_width*w+500, heigh=h_width*h+30, bg="white")
# cvs.create_text(800,300,text="三目並べDX",fill="navy",font=("Times New Roman",60))
# 縦のグリッド線を描画
for i in range(h+1):
    cvs.create_line(10, 10+h_width*i, 10+w_width*w,
                    10+h_width*i, fill="black", width=3)
# 横のグリッド線を描画
for i in range(w+1):
    cvs.create_line(10+w_width*i, 10, 10+w_width*i,
                    10+h_width*h, fill="black", width=3)

id = [[0]*shoku, [0]*shoku] # 4 (職人の数) * 2 の二次元配列作成

for i in range(h):
    for j in range(w):
        if a[0][i][j]//10 == 3:
            cvs.create_rectangle(21+j*w_width, 17+i*h_width, (j+1)
                                 * w_width, 4+(i+1)*h_width, fill="black", width=0)
        if a[0][i][j]//100 == 4:
            cvs.create_rectangle(12+j*w_width, 12+i*h_width, 9+(j+1) *
                                w_width, 9+(i+1)*h_width, fill="yellow", width=0, tag="400")
        if a[0][i][j] % 100//10 == 1:
            id[0][a[0][i][j] % 10] = cvs.create_oval(13+j*w_width+w_h, 13+i*h_width, 7+(
                j+1)*w_width-w_h, 7+(i+1)*h_width, fill=color[0], width=0, tag="s1")
        if a[0][i][j] % 100//10 == 2:
            id[1][a[0][i][j] % 10] = cvs.create_oval(13+j*w_width+w_h, 13+i*h_width, 7+(
                j+1)*w_width-w_h, 7+(i+1)*h_width, fill=color[1], width=0, tag="s2")
cvs.itemconfig(id[0][0], fill=color[2])
cvs.lift("s1")
cvs.lift("s2")
# cvs.lower("400")
# fg=cvs.create_rectangle(0,0,500,500,fill="#aaaaff")
# cvs.lower(fg)

# ボタン作成
rightt = 10+w_width*w
wspace = 30
hspace = 30
www = 110
hhh = 70
bu = [0]*4
but = [0]*9
bu[0] = tk.Button(text="滞在", bg="red", command=lambda: action(0))
bu[0].place(x=rightt+wspace, y=hspace, width=www, heigh=hhh)
bu[1] = tk.Button(text="移動", bg="white", command=lambda: action(1))
bu[1].place(x=rightt+wspace, y=hspace+hhh, width=www, heigh=hhh)
bu[2] = tk.Button(text="建築", bg="white", command=lambda: action(2))
bu[2].place(x=rightt+wspace, y=hspace+hhh*2, width=www, heigh=hhh)
bu[3] = tk.Button(text="解体", bg="white", command=lambda: action(3))
bu[3].place(x=rightt+wspace, y=hspace+hhh*3, width=www, heigh=hhh)
but[0] = tk.Button(text='↖', bg='gray', command=lambda: bector(0))
but[0].place(x=rightt+wspace*2+www, y=hspace, width=www, heigh=hhh)
but[1] = tk.Button(text='↑', bg='white', command=lambda: bector(1))
but[1].place(x=rightt+wspace*2+www*2, y=hspace, width=www, heigh=hhh)
but[2] = tk.Button(text='↗', bg='white', command=lambda: bector(2))
but[2].place(x=rightt+wspace*2+www*3, y=hspace, width=www, heigh=hhh)
but[3] = tk.Button(text='←', bg='white', command=lambda: bector(3))
but[3].place(x=rightt+wspace*2+www, y=hspace+hhh, width=www, heigh=hhh)
but[5] = tk.Button(text='→', bg='white', command=lambda: bector(5))
but[5].place(x=rightt+wspace*2+www*3, y=hspace+hhh, width=www, heigh=hhh)
but[6] = tk.Button(text='↙', bg='white', command=lambda: bector(6))
but[6].place(x=rightt+wspace*2+www, y=hspace+hhh*2, width=www, heigh=hhh)
but[7] = tk.Button(text='↓', bg='white', command=lambda: bector(7))
but[7].place(x=rightt+wspace*2+www*2, y=hspace+hhh*2, width=www, heigh=hhh)
but[8] = tk.Button(text='↘', bg='white', command=lambda: bector(8))
but[8].place(x=rightt+wspace*2+www*3, y=hspace+hhh*2, width=www, heigh=hhh)
enter = tk.Button(text='確定', bg='gray', command=submit)
enter.place(x=rightt+wspace*2+www*2, y=hspace+hhh, width=www, height=hhh)
txt = cvs.create_text(rightt+wspace*2+www*2.5, hspace +
                    hhh*3.5, text="残りターン数 "+str(turn), font=("", 24))
cvs.update()
cvs.pack()
root.bind("<Button>", click)
root.mainloop()
