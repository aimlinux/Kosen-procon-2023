# ====================
# 三目並べ
# ====================

# パッケージのインポート
import random
import math
import numpy as np

# ゲーム状態
class State:
    # 初期化
    def __init__(self, pieces, enemy_pieces,agent,p,turn,a,b,jon,point,sh,key = False):
        # 石の配置
        if key:
            a=[[[0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0], [0, 10, 0, 0, 30, 0, 30, 0, 0, 12, 0], [0, 0, 400, 0, 30, 21, 30, 0, 400, 0, 0], [0, 0, 0, 30, 0, 0, 0, 30, 0, 0, 0], [0, 30, 30, 0, 400, 0, 400, 0, 30, 30, 0], [30, 0, 20, 0, 0, 400, 0, 0, 23, 0, 30], [0, 30, 30, 0, 400, 0, 400, 0, 30, 30, 0], [0, 0, 0, 30, 0, 0, 0, 30, 0, 0, 0], [0, 0, 400, 0, 30, 22, 30, 0, 400, 0, 0], [0, 11, 0, 0, 30, 0, 30, 0, 0, 13, 0], [0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
            sh=[[[1, 1], [1, 9], [9, 1], [9, 9]], [[2, 5], [5, 2], [5, 8], [8, 5]]]
            agent = [[],[]]
            for i in range(2):
                for j in range(4):
                    agent[i].append(np.zeros_like(a[0]))
                    agent[i][j][sh[i][j][0]][sh[i][j][1]] = 1
            
            pieces = np.zeros_like(a[0])
            enemy_pieces = pieces
            p = 0
            turn = 50
            jon = [0,0]
            point= [0,0]
            b =  np.zeros_like(a[0])


        self.w = 11
        self.kodojun = [0,3,2,1]
        self.shoku = 4
        self.ike = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
        
        self.siro = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        

        self.pieces = pieces
        self.enemy_pieces = enemy_pieces
        self.agent = agent
        self.sh=sh
        self.turn = turn
        self.p = p
        self.b = b
        self.a = a
        self.jon = jon
        self.point=point
        


    def reset(self):
        self.sh=[[[1, 1], [1, 9], [9, 1], [9, 9]], [[2, 5], [5, 2], [5, 8], [8, 5]]]
        self.turn = 50
        self.p = 0
        self.a=[[[0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0], [0, 10, 0, 0, 30, 0, 30, 0, 0, 12, 0], [0, 0, 400, 0, 30, 21, 30, 0, 400, 0, 0], [0, 0, 0, 30, 0, 0, 0, 30, 0, 0, 0], [0, 30, 30, 0, 400, 0, 400, 0, 30, 30, 0], [30, 0, 20, 0, 0, 400, 0, 0, 23, 0, 30], [0, 30, 30, 0, 400, 0, 400, 0, 30, 30, 0], [0, 0, 0, 30, 0, 0, 0, 30, 0, 0, 0], [0, 0, 400, 0, 30, 22, 30, 0, 400, 0, 0], [0, 11, 0, 0, 30, 0, 30, 0, 0, 13, 0], [0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
        self.b = np.zeros_like(self.a[0])
        self.jon = [0,0]
        self.point=[0,0]
        self.pieces = np.zeros_like(self.a[0])
        self.enemy_pieces = np.zeros_like(self.a[0])
        self.agent = np.zeros_like(self.a[0])
        self.enemy_agent = np.zeros_like(self.a[0])
        for i in range(4):
            self.agent[self.sh[0][i][0]][self.sh[0][i][1]] = 1
            self.enemy_agent[self.sh[1][i][0]][self.sh[1][i][1]] = 1

        return np.array([self.pieces,self.agent,self.enemy_pieces,self.enemy_agent])


    # # 石の数の取得
    # def piece_count(self, pieces):
    #     count = 0
    #     for i in pieces:
    #         if i == 1:
    #             count +=  1
    #     return count

    # 負けかどうか
    def is_lose(self):
        if self.turn <= 1:
            if self.point[0] > self.point[1]:
                return True
            
        return False


    # 引き分けかどうか
    def is_draw(self):
        if self.turn <= 1:
            if self.point[0] == self.point[1]:
                return True
        
        return False

    # ゲーム終了かどうか
    def is_done(self):
        if self.turn == 1:
            return True
        else: return False

    # 次の状態の取得
    def next(self, action):
        print(action)
        bec = self.bector(action)
        act = self.action(action)
        for j in self.kodojun:
            for i in range(self.shoku):
                shx = self.sh[self.p][i][0]
                shy = self.sh[self.p][i][1]
                ax = shx+bec[i] % 3-1
                ay = shy+bec[i]//3-1

                if act[i] == 0:     #滞在
                    pass
                
                elif act[i]==j and j==1:    #移動
                    if ax >= 0 and ax < self.w and ay >= 0 and ay < self.w:
                        if self.a[0][ay][ax] == 0 or self.a[0][ay][ax] == 400 or (self.a[0][ay][ax]//100000 == (self.p+1) and self.a[0][ay][ax]%100//10 != 3):
                            self.sh[self.p][i][0] = ax
                            self.sh[self.p][i][1] = ay
                            self.a[0][ay][ax] += (self.p+1)*10+i
                            self.a[0][shy][shx] -= (self.p+1)*10+i
                            self.agent[self.p][i][ay][ax] = 1
                            self.agent[self.p][i][shy][shx] = 0



                elif act[i] == j and j == 2:    #建築
                    if ax >= 0 and ax < self.w and ay >= 0 and ay < self.w and bec[i] % 2 == 1:
                        n = self.a[0][ay][ax]
                        if n//100 == 0 and n/10 % 10 != 2-self.p:
                            self.a[0][ay][ax] += (self.p+1) * 100000+self.jon[self.p]*100
                            self.jon[self.p] += 1
                            self.a[self.p+1][ay][ax] = self.jon[self.p]*10
                            if self.p == 0:
                                self.pieces[ax][ay] += 1
                            if self.p == 1:
                                self.enemy_pieces[ax][ay] += 1
                        
                elif act[i]==j and j == 3:  # 解体
                    if ax >= 0 and ax < self.w and ay >= 0 and ay < self.w and bec[i] % 2 == 1:
                        n = self.a[0][ay][ax]
                        if n//100000 != 0:
                            self.a[0][ay][ax] = n % 100
                            self.a[n//100000][ay][ax] = 0
                            if self.pieces[ax][ay]// 10 == 1:self.pieces[ax][ay] -= 1
                            if self.enemy_pieces[ax][ay]// 10 == 1:self.pieces[ax][ay] -= 1
        
        aa = np.array(self.a[self.p+1])
        for i in range(np.shape(self.a)[1]):
            if aa[i][0] == 0:
                aa[i][0] = -1
            if aa[i][-1] == 0:
                aa[i][-1] = -1
            for j in range(np.shape(self.a)[2]):
                if aa[i][j]!=0 and aa[i][j]%10==0:
                    aa[i][j] = 10
                if aa[i][j] == 5:
                    aa[i][j] = 0
        for j in range(np.shape(self.a)[2]):
            if aa[0][j] == 0:
                aa[0][j] = -1
            if aa[-1][j] == 0:
                aa[-1][j] = -1

        self.turn -= 1
        self.takumi = 0
        area = np.zeros_like(aa)
        n = 1
        ax = 0
        ay = 0
        for i in range(np.shape(aa)[0]-ay-2):
            for j in range(np.shape(aa)[1]-ax-2):
                if aa[ax+j+1][ay+i+1] == 0:
                    area,n,aa = self.jinti(ax+j+1,ay+i+1,aa,area,n)
                ax = 0

        

        self.pt(aa)
        self.p = 1-self.p
        return State( self.pieces, self.enemy_pieces,self.agent,self.p,self.turn,self.a,self.b,self.jon,self.point,self.sh)

    def bector(self,action):
        bec = [0]*self.shoku
        for i in range(len(bec)):
            bec[i] = action[i]%10
        return bec
    
    def  action(self,action):
        act = [0]*self.shoku
        for i in range(len(act)):
            act[i] = action[i]//10
        return act
    
    def jinti(self,ax,ay,aa,area,n):
        an = np.array([0,0,0,0])

        if aa[ax][ay-1] == -1:
            aa[ax][ay] = -1
        elif aa[ax+1][ay] == -1:
            aa[ax][ay] = -1
        elif aa[ax][ay+1] == -1:
            aa[ax][ay] = -1
        elif aa[ax-1][ay] == -1:
            aa[ax][ay] = -1
        
        if aa[ax][ay-1]!=10 and aa[ax][ay-1]!=-1:
            an[0] = area[ax][ay-1]
        if aa[ax+1][ay]!=10 and aa[ax+1][ay]!=-1:
            an[1] = area[ax+1][ay]
        if aa[ax][ay+1]!=10 and aa[ax][ay+1]!=-1:
            an[2] = area[ax][ay+1]
        if aa[ax-1][ay]!=10 and aa[ax-1][ay]!=-1:
            an[3] = area[ax-1][ay]

        if aa[ax][ay] == -1:
            for i in range(np.shape(area)[0]):
                for j in range(np.shape(area)[1]):
                    if area[i][j]!=0 and aa[i][j]!=-1 and aa[i][j]!=10:
                        for k in an:
                            if area[i][j] == k:aa[i][j] = -1

                

        else:
            if np.all(an == np.array([0,0,0,0])):
                area[ax][ay] = n
                n += 1
                if n == 10:n+=1
            
            else:
                an = np.sort(an)
                area[ax][ay] = an[3]
                for i in range(3):
                    if an[i]!=an[i+1] and an[i]!=0:
                        for l in range(np.shape(area)[0]):
                            for j in range(np.shape(area)[1]):
                                if area[l][j] == an[i+1]:
                                    area[l][j] = an[i]
                        an[i+1] = an[i]

        return area,n,aa

    def pt(self,aa):
        self.point[self.p] = 0
        for i in range(self.w):
            for j in range(self.w):
                if aa[i][j] == 0:
                    self.a[self.p+1][i][j] = 5
                if aa[i][j] == 10 :self.point[self.p] += 10
                if self.a[self.p+1][i][j] == 5:
                    if aa[i][j] == 0: 
                        if self.a[0][i][j]//100%10 == 4:self.point[self.p] += 130
                        else:self.point[self.p] += 30
                    elif self.b[i][j] == -1:
                        if self.a[0][i][j]//100%10 == 4: self.point[self.p] +=130
                        else:self.point[self.p] += 30            
                    else: self.a[self.p+1][i][j] = 0
        self.b = aa

        return self.point

    # 合法手のリストの取得
    def legal_actions(self):
        #　合法手を調べる
        las = []
        ln = 1

        #　職人の位置
        shx = [0]*self.shoku 
        shy = [0]*self.shoku
        for i in range(self.shoku): # 職人の位置を格納
                shx[i] = self.sh[self.p][i][0]
                shy[i] = self.sh[self.p][i][1]


        #　合法手を調べる
        for j in range(self.shoku):
            la = []
            

            #　移動
            for i in range(9):
                ax = shx[j] + i % 3-1
                ay = shy[j] + i // 3-1

                #　移動
                if ax >= 0 and ax < self.w and ay >= 0 and ay < self.w:
                    if self.a[0][ay][ax] == 0 or self.a[0][ay][ax] == 400 or (self.a[0][ay][ax]//100000 == (self.p+1) and self.a[0][ay][ax]%100//10 != 3):
                        la.append(10+i)
                    

                #  建築
                if ax >= 0 and ax < self.w and ay >= 0 and ay < self.w and i % 2 == 1:
                        n = self.a[0][ay][ax]
                        if n//100 == 0 and n/10 % 10 != 2-self.p:
                            la.append(20+i)
                #　解体
                        elif n//100000 == 2-self.p:
                            la.append(30+i)
                    
            # リストの要素を枝狩りする
            for ele in la[:]:
                if ele == 14: # 滞在(14)
                    la.remove(ele)
                else:
                    continue
                    
                
                    
            las.append(la)
            
            # las : 各職人ごとに可能な合法手のリストを格納するためのリスト
            # la : 特定の職人が行う可能性のあるアクションが格納されるリスト
            # -------- アクションの種類 --------
            # 移動 : 10(左上), 11(上), 12(右上), 13(左), 14(滞在), 15(右), 16(左下), 17(下), 18(右下)
            # 建築 : ・・ {上下左右のみ}
            # 解体 : ・・ {上下左右のみ}
            
        for i in range(len(las)):
            ln = ln * len(las[i])
        
        actions = [] 
        n = [0 for _ in range(self.shoku)]
        for _ in range(ln):
            actions.append([las[i][n[i]] for i in range(self.shoku)])
            n[-1]+=1
            for j in range(self.shoku-1):
                if n[-1*j-1] == len(las[-1*j-1]):
                    n[-1*j-2] += 1
                    n[-1*j-1] = 0
            
            # 滞在、一番恥とか
        
        # 生成されたactionsリストから100~199までの要素を取得し新しいリストとして返す。
        # テスト用らしい
        return actions[100:200] 

    # 先手かどうか
    def is_first_player(self):
        return self.turn%2 == 0

    # 文字列表示
    def s(self):
        
        return self.a[0]

# ランダムで行動選択
    def random_action(state):
        legal_actions = state.legal_actions()
        return legal_actions[random.randint(0, len(legal_actions)-1)]

# アルファベータ法で状態価値計算
def alpha_beta(state, alpha, beta):
    # 負けは状態価値-1
    if state.is_lose():
        return -1

    # 引き分けは状態価値0
    if state.is_draw():
        return  0

    # 合法手の状態価値の計算
    for action in state.legal_actions():
        score = -alpha_beta(state.next(action), -beta, -alpha)
        if score > alpha:
            alpha = score

        # 現ノードのベストスコアが親ノードを超えたら探索終了
        if alpha >= beta:
            return alpha

    # 合法手の状態価値の最大値を返す
    return alpha

# アルファベータ法で行動選択
def alpha_beta_action(state):
    # 合法手の状態価値の計算
    best_action = 0
    alpha = -float('inf')
    for action in state.legal_actions():
        score = -alpha_beta(state.next(action), -float('inf'), -alpha)
        if score > alpha:
            best_action = action
            alpha = score

    # 合法手の状態価値の最大値を持つ行動を返す
    return best_action

# プレイアウト
def playout(state):
    # 負けは状態価値-1
    if state.is_lose():
        return -1

    # 引き分けは状態価値0
    if state.is_draw():
        return  0

    # 次の状態の状態価値
    return -playout(state.next(state.random_action(state)))

# 最大値のインデックスを返す
def argmax(collection):
    return collection.index(max(collection))

# モンテカルロ木探索の行動選択
def mcts_action(state):
    # モンテカルロ木探索のノード
    class node:
        # 初期化
        def __init__(self, state):
            self.state = state # 状態
            self.w = 0 # 累計価値
            self.n = 0 # 試行回数
            self.child_nodes = None  # 子ノード群

        # 評価
        def evaluate(self):
            # ゲーム終了時
            if self.state.is_done():
                # 勝敗結果で価値を取得
                value = -1 if self.state.is_lose() else 0 # 負けは-1、引き分けは0

                # 累計価値と試行回数の更新
                self.w += value
                self.n += 1
                return value

            # 子ノードが存在しない時
            if not self.child_nodes:
                # プレイアウトで価値を取得
                value = playout(self.state)

                # 累計価値と試行回数の更新
                self.w += value
                self.n += 1

                # 子ノードの展開
                if self.n == 10:
                    self.expand()
                return value

            # 子ノードが存在する時
            else:
                # UCB1が最大の子ノードの評価で価値を取得
                value = -self.next_child_node().evaluate()

                # 累計価値と試行回数の更新
                self.w += value
                self.n += 1
                return value

        # 子ノードの展開
        def expand(self):
            legal_actions = self.state.legal_actions()
            self.child_nodes = []
            for action in legal_actions:
                self.child_nodes.append(node(self.state.next(action)))

        # UCB1が最大の子ノードを取得
        def next_child_node(self):
             # 試行回数nが0の子ノードを返す
            for child_node in self.child_nodes:
                if child_node.n == 0:
                    return child_node

            # UCB1の計算
            t = 0
            for c in self.child_nodes:
                t += c.n
            ucb1_values = []
            for child_node in self.child_nodes:
                ucb1_values.append(-child_node.w/child_node.n+2*(2*math.log(t)/child_node.n)**0.5)

            # UCB1が最大の子ノードを返す
            return self.child_nodes[argmax(ucb1_values)]

    # ルートノードの生成
    root_node = node(state)
    root_node.expand()

    # ルートノードを100回評価
    for _ in range(100):
        root_node.evaluate()

    # 試行回数の最大値を持つ行動を返す
    legal_actions = state.legal_actions()
    n_list = []
    for c in root_node.child_nodes:
        n_list.append(c.n)
    return legal_actions[argmax(n_list)]

# 動作確認
if __name__ == '__main__':
    # 状態の生成
    state = State(None,None,None,None,None,None,None,None,None,None,True)

    # ゲーム終了までのループ
    while True:
        # ゲーム終了時
        if state.is_done():
            break

        # 次の状態の取得
        state = state.next(state.random_action())

        # 文字列表示
        print(state.point)
        print()