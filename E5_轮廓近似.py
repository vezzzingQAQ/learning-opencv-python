'''
2021.1.30FromIvicxDS:openCV;E5图像形态处理：轮廓近似
'''
'''
不断二分检测曲线上的点到两个端点连线段的距离是否小于阈值
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

img=cv2.imread("image/B2.jpg")
grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转化为灰度图
ret,thresh=cv2.threshold(grayImage,200,255,cv2.THRESH_BINARY)#转化为二值图

contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#[做完二值的结果]【报错?】，轮廓信息，轮廓层级
cnt=contours[1]

draw_img=img.copy()
res=cv2.drawContours(draw_img,[cnt],-1,(0,0,255),2)
showPicture("res",res)

#轮廓近似>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
elsilon=0.05*cv2.arcLength(cnt,True)#周长的10%
approx=cv2.approxPolyDP(cnt,elsilon,True)#设置轮廓近似的阈值
draw_img=img.copy()
res=cv2.drawContours(draw_img,[approx],-1,(0,0,255),2)
showPicture("approx",res)


