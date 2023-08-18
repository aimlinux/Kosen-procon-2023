import csv
import cv2
import numpy as np

alpha=["A","B","C"]
masu=[11,13,15,17,21,25]
size=(1920,960)
for i in alpha:
    for j in masu:
        f=open("../"+i+str(j)+".csv","r")
        field=csv.reader(f)
        img=np.zeros((j,j,3))
        k=0
        for row in field:
            for l in range(j):
                #print(field[k][l])
                if row[l]=="0":
                    img[k][l]=[255,255,255]
                elif row[l]=="2":
                    img[k][l]=[0,255,255]
                elif row[l]=="a":
                    img[k][l]=[0,0,255]
                elif row[l]=="b":
                    img[k][l]=[255,0,0]
            k+=1
        img_resize = cv2.resize(img,   # 画像データを指定
                               size,   # リサイズ後のサイズを指定
                               interpolation=cv2.INTER_NEAREST)
        # cv2.imshow(i+str(j),img_resize)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        if cv2.imwrite(i+str(j)+".png",img_resize)==False:
            print("None")

# file=".\\フィールドデータ\\A11.csv"
# f=open(file,"r")
# field=csv.reader(f)
# for i in field:
#     print(i)
# f.close

# #img = cv2.imread("11a.png")
# #print(type(img))
# img=np.zeros((3,3,3))
# img[0][1][2]=255
# # サイズ設定｜cv2では(幅、高さ）の順で数値を設定
# size = (1920,960)

# # リサイズ
# img_resize = cv2.resize(img,   # 画像データを指定
#                         size,   # リサイズ後のサイズを指定
#                        interpolation=cv2.INTER_NEAREST)

# cv2.imwrite("abc.png",img_resize)
