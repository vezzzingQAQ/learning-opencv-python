'''
2021.1.29FromIvicxDS:openCV;E2平滑处理
'''
'''
平均卷积操作【均值滤波】
构造卷积矩阵求内积
'''
import cv2#读取格式为BGR
import numpy

def showPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/Noise.jpg")
showPicture("OriginalPicture",img)

#均值滤波**********************
#  □□□
#  □■□
#  □□□
blur=cv2.blur(img,(3,3))#指定卷积矩阵的大小，通常是奇数【中心点】
showPicture("BluredPicture",blur)

#方框滤波**********************
box1=cv2.boxFilter(img,-1,(3,3),normalize=True)
#执行归一化(/9)结果与均值滤波相同
showPicture("BoxNormalized",box1)

box2=cv2.boxFilter(img,-1,(3,3),normalize=False)
#不执行归一化(/9)结果直接相加越界当做255
showPicture("BoxInnormalized",box2)

#高斯滤波**********************
#_/\_高斯函数
"""
[0.6,0.8,0.6
 0.8,1  ,0.8
 0.6,0.8,0.6]
按照距离赋予权重
"""
aussian=cv2.GaussianBlur(img,(5,5),1)
showPicture("GaussianBlur",aussian)

#中值滤波**********************
#矩阵内的数从小到大排序去中间值
median=cv2.medianBlur(img,5)
showPicture("medianBlur",median)#当有噪音点时可以完全过滤

res1=numpy.hstack((img,blur,box1))
res2=numpy.hstack((box2,aussian,median))
res=numpy.vstack((res1,res2))
showPicture("totalProcess",res)