'''
2021.1.28FromIvicxDS:openCV;E1图像的基本操作
'''
'''
1.图像运算
2.改变图像大小
3.图像融合
'''
import cv2#读取格式为BGR

def showPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/P3.jpg")
img2=img+10

print(img)
print("**********")
print(img2)
print(">>>>>>>>>>>>>>>>>>>>")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#运算叠加两张图片与。added的区别（封顶）
img3=cv2.imread("image/add1.jpg")
img3=cv2.resize(img3,(300,300))
img4=cv2.imread("image/add2.jpg")#resize强制放缩
img4=cv2.resize(img4,(300,300))
print(img3)
print("**********")
print(img4)
print(">>>>>>>>>>>>>>>>>>>>")

imgadded1=img3+img4
print(imgadded1)
showPicture("image add",imgadded1)
print(">>>>>>>>>>>>>>>>>>>>")

imgadded2=cv2.add(img3,img4)
print(imgadded2)
showPicture("image add2",imgadded2)

imagemesh=cv2.addWeighted(img3,0.4,img4,0.6,0)#图像按照权重融合
showPicture("image mesh",imagemesh)#R=a*x1+b*x2+c

#图像按比例缩放
img5=cv2.imread("image/P1.jpg")
img5=cv2.resize(img5,(0,0),fx=2,fy=0.3)
showPicture("image process",img5)
