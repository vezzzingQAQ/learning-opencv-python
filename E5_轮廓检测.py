'''
2021.1.30FromIvicxDS:openCV;E5图像形态处理：轮廓检测
'''
'''
cv2.findContours(img,mode,method)
mode:轮廓检测模式
RETR_TREE:检测所有轮廓,并重构嵌套轮廓的整个层次【保留所有轮廓信息,最常用】
method:轮廓逼近方法
CHAIN_APPROX_NONE:以Freeman链码方式输出轮廓【长方形保留所有边】
CHAIN_APPROX_SIMPLE:压缩,结果更精简计算速度快【长方形保留四个顶点】

使用二值图像
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

img=cv2.imread("image/B1.jpg")#轮廓检测
grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图
ret,thresh=cv2.threshold(grayImage,200,255,cv2.THRESH_BINARY)#转化为二值图
showPicture("thresh",thresh)

contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#[做完二值的结果]【报错?】，轮廓信息，轮廓层级

#绘制轮廓
draw_img1=img.copy()#防止后一步修改原图
draw_img2=img.copy()#防止后一步修改原图
draw_img3=img.copy()#防止后一步修改原图
draw_img4=img.copy()#防止后一步修改原图
draw_img5=img.copy()#防止后一步修改原图
draw_img6=img.copy()#防止后一步修改原图

#↓参数说明:原图，轮廓信息，绘制轮廓的层级【-1表示描绘所有】，画的颜色BGR,画的粗细
r1=cv2.drawContours(draw_img1,contours,-1,(255,0,255),2)
r2=cv2.drawContours(draw_img2,contours,0,(255,0,255),2)
r3=cv2.drawContours(draw_img3,contours,1,(255,0,255),2)
r4=cv2.drawContours(draw_img4,contours,2,(255,0,255),2)
r5=cv2.drawContours(draw_img5,contours,3,(255,0,255),2)
r6=cv2.drawContours(draw_img6,contours,4,(255,0,255),2)
res1=numpy.hstack((r1,r2,r3))
res2=numpy.hstack((r4,r5,r6))
res=numpy.vstack((res1,res2))
showPicture("contour",res)

#轮廓特征提取***********************************************************
#计算图形面积
cnt=contours[2]
print(cv2.contourArea(cnt))
#计算周长，True表示闭合的
print(cv2.arcLength(cnt,True))

