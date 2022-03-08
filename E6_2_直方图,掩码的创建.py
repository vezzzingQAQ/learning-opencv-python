'''
2021.1.31FromIvicxDS:openCV;E6：直方图,掩码的创建
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

def showPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/C2.jpg")#灰度图
print(img.shape)

#构建一个MASK掩码>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
mask=numpy.zeros(img.shape[:2],numpy.uint8)#八位灰度图
print(mask.shape)
mask[0:300,100:400]=255#要保留的位置设为白色
showPicture("maskedImage",mask)

#用与操作使得掩码生效>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
masked_img=cv2.bitwise_and(img,img,mask=mask)
showPicture("masked_img",masked_img)
