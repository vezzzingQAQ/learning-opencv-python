'''
2021.1.29FromIvicxDS:openCV;E2图像形态处理：梯度运算
'''
'''
对图像
膨胀
腐蚀
膨胀结果-腐蚀结果->轮廓信息【膨胀腐蚀后一样的地方(图形内,背景)相减后为0】
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

kernel=numpy.ones((3,3),numpy.uint8)
img=cv2.imread("image/kernel.jpg")

dilate=cv2.dilate(img,kernel,iterations=1)
erosion=cv2.erode(img,kernel,iterations=1)

result=dilate-erosion
res1=numpy.hstack((img,result))
res2=numpy.hstack((dilate,erosion))
res=numpy.vstack((res1,res2))
showPicture("",res)