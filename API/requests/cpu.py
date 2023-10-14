import random as rnd
def cpu(env,n):
    shx = env.sh[env.p][n][0]
    shy = env.sh[env.p][n][1]
    if env.cp==1:
        if env.f[0]=="C" and env.f[1]=="1":# C系
            if env.p==0:
                if n==env.shoku-2 and env.turn > env.maxturn-2:
                    return 1,2
                if n==env.shoku-1 and env.turn > env.maxturn-10 and shy!=env.h//2-2:
                    return 1,7+(shx!=env.w//2+2)
            if env.p==1:
                if n==1 and env.turn > env.maxturn-2:
                    return 1,6
                if n==0 and env.turn > env.maxturn-10 and shy!=env.h//2+2:
                    return 1,(shx==env.w//2-2)
        for i in [1,3,5,7]:# 相手の城壁を解体
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.a[2-env.p][ay][ax]>5 and env.cpu_a[ay][ax]//1000!=env.turn*10+3:
                    print("解体")
                    return 3,i
        if env.a[0][shy][shx]//100==4 and env.a[1+env.p][shy][shx]!=5:# 城にいるとき建築
            for i in [1,3,5,7]:
                ax = shx+i % 3-1
                ay = shy+i//3-1
                if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                    if env.a[0][ay][ax]//100 == 0 and env.a[0][ay][ax]//10 % 10 != 2-env.p and env.a[1+env.p][ay][ax]==0 and env.cpu_a[ay][ax]//1000!=env.turn*10+2:
                        print("城建築")
                        return 2,i
        if env.f=="C11" and env.turn>env.maxturn-24:# C11
            if env.p==0 and n==env.shoku-2:
                for i in [5,8,2]:
                    ax = shx+i % 3-1
                    ay = shy+i//3-1
                    if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                        if env.a[0][shy+i//3-1][shx+i%3-1]%100==0 and env.a[1][shy+i//3-1][shx+i%3-1]>5:
                            return 1,i
            if env.p==1 and n==1:
                for i in [3,0,6]:
                    ax = shx+i % 3-1
                    ay = shy+i//3-1
                    if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                        if env.a[0][shy+i//3-1][shx+i%3-1]%100==0 and env.a[2][shy+i//3-1][shx+i%3-1]>5 and env.cpu_a[ay][ax]//1000!=env.turn*10+1:
                            return 1,i
        for i in [0,1,8,2,6,3,5,7]:# 城に移動
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.a[0][ay][ax]==400 and env.a[1+env.p][ay][ax]==0 and env.a[0][ay][ax]%100==0 and env.cpu_a[ay][ax]//1000!=env.turn*10+1 and env.cpu_a[ay][ax]%10!=env.p+1:
                    print("城移動")
                    return 1,i
        if env.a[1+env.p][shy][shx]==0:# 4方向に城壁があれば建築
            if 0<shx<env.w-1 and 0<shy<env.h-1:
                if env.a[1+env.p][shy+1][shx]>5 or env.a[1+env.p][shy-1][shx]>5 or env.a[1+env.p][shy][shx+1]>5 or env.a[1+env.p][shy][shx-1]>5:
                    for i in [1,3,5,7]:
                        ax = shx+i % 3-1
                        ay = shy+i//3-1
                        if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                            if env.a[0][ay][ax]//100==0 and env.a[0][ay][ax]//10!=2-env.p and env.a[1+env.p][ay][ax]==0 and env.cpu_a[ay][ax]//1000!=env.turn*10+2:
                                print("城壁建築")
                                return 2,i
        else:# 斜め移動 中央優先
            mini=(shx<env.w//2)+(shy>=env.h//2)*3
            if abs(shx-env.w//2)<abs(shy-env.h//2):
                mini=(shx>=env.w//2)+(shy<env.h//2)*3
            for i in [(shx<env.w//2)+(shy<env.h//2)*3,mini,4-mini,(shx>=env.w//2)+(shy>=env.h//2)*3]:
                ax = shx+i*2 % 3-1
                ay = shy+i*2//3-1
                if ax >= 1 and ax < env.w-1 and ay >= 1 and ay < env.h-1:
                    if env.a[0][ay][ax]%100==0 and env.a[2-env.p][ay][ax]<6 and env.a[1+env.p][ay][ax]!=5 and env.cpu_a[ay][ax]//1000!=env.turn*10+1  and env.cpu_a[ay][ax]%10!=env.p+1:
                        print("斜め移動",i*2)
                        return 1,i*2
        mini=(shx<env.w//2)*2+3
        if abs(shx-env.w)<abs(shy-env.h):
            mini=(shy<env.h//2)*6+1
        for i in [(shx<env.w//2)*2+(shy<env.h//2)*6,mini,(shx<env.w//2)*2+(shy<env.h//2)*6+4-mini]:# 中央へ移動
            print(i)
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.a[0][ay][ax]%100==0 and env.a[2-env.p][ay][ax]<6 and env.cpu_a[ay][ax]//1000!=env.turn*10+1 and env.cpu_a[ay][ax]%10!=env.p+1:
                   print("中央移動")
                   return 1,i
        for i in [1,3,5,7]:# とりあえず建築
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.a[0][ay][ax]//10!=2-env.p and env.a[0][ay][ax]//100==0 and env.a[1+env.p][ay][ax]==0 and env.cpu_a[ay][ax]//1000!=env.turn*10+2:
                    print("建築しかすることねえ",i)
                    return 2,i
        list=[0,1,2,3,5,6,7,8]
        rnd.shuffle(list)
        for i in list:
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.a[0][ay][ax]%100==0 and env.a[2-env.p][ay][ax]<6 and env.cpu_a[ay][ax]//1000!=env.turn*10+1:
                   print("散歩")
                   return 1,i
        print("暇")
        return 0,0#滞在
    if env.cp==2:
        for i in [1,3,5,7]:# 相手の城壁を解体
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.a[2-env.p][ay][ax]>5 and env.cpu_a[ay][ax]//1000!=env.turn*10+3:
                    print("解体")
                    return 3,i
        for i in [1,3,5,7]:
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.cpu_a[ay][ax]//1000!=env.turn*10+2 and env.cpu_a[ay][ax]//1000%10>1 and env.a[0][ay][ax]//100==0 and env.a[0][ay][ax]%100//10!=2-env.p:
                    print("妨害")
                    return 2,i
        bool1=True
        for i in [0,1,2,3,5,6,7,8]:
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.a[0][ay][ax]%100//10==2-env.p:
                    bool1=False
        if bool1:
            a1=[[0]*env.w for i in range(env.h)]
            a2=[[shy,shx]]
            k=1
            a1[shy][shx]=k
            bool0=True
            while bool0:
                k+=1
                a3=[]
                for i in a2:
                    for j in [0,1,2,3,5,6,7,8]:
                        ax = i[1]+j % 3-1
                        ay = i[0]+j//3-1
                        if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                            if a1[ay][ax]==0 and (j%2!=0 or env.a[2-env.p][ay][ax]<6):
                                if env.a[0][ay][ax]!=30:
                                    a1[ay][ax]=k
                                    a3=a3+[[ay,ax]]
                                if env.a[0][ay][ax]%100//10==2-env.p:
                                    bool0=False
                                    a4=[ay,ax]
                a2=a3
            for i in range(k-2):
                for j in [0,1,2,3,5,6,7,8]:
                    ax = a4[1]+j % 3-1
                    ay = a4[0]+j//3-1
                    if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                        if a1[ay][ax]==k-i-1:
                            a4=[ay,ax]
                            break
            # if n==0:
                # for i in range(env.h):
                #     print(a1[i])
                # print("\n")
            print("追従")
            return 1,(ax-shx+1)+(ay-shy+1)*3
        for i in [1,3,5,7]:# とりあえず建築
            ax = shx+i % 3-1
            ay = shy+i//3-1
            if ax >= 0 and ax < env.w and ay >= 0 and ay < env.h:
                if env.a[0][ay][ax]//10!=2-env.p and env.a[0][ay][ax]//100==0 and env.a[1+env.p][ay][ax]==0 and env.cpu_a[ay][ax]//1000!=env.turn*10+2:
                    print("建築しかすることね",i)
                    return 2,i
        print("滞・在")
        return 0,0