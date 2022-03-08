'''
2021.1.31FromIvicxDS:openCV;E6：直方图
'''
'''
读取灰度图，根据相应灰度值的像素点数绘制直方图
cv2.calcHist(images,channels,mask,histSize,ranges)
*所有参数传入要用中括号[images]
images:
channels:BGR[0],[1],[2]
mask:指定图像的一个区域进行统计
histSize:指定取值的宽度ex0-10画一条，默认256
range:256
'''
import cv2#读取格式为BGR
import numpy
from matplotlib import pyplot as plt

def showPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/C2.jpg")
color=("b","g","r")
for i,col in enumerate(color):
    histr=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])

plt.show()


