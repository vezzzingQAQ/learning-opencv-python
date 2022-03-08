'''
2021.1.31FromIvicxDS:openCV;E6：直方图,直方图均衡化
'''
'''
将图片分成小格分别做均衡化防止图片中细节丢失
【涉及对格子的边界处理】
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

img=cv2.imread("image/x1.jpg",0)

clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))

equ_img=cv2.equalizeHist(img)
clahe_img=clahe.apply(img)
res=numpy.hstack((img,equ_img,clahe_img))

showPicture("equalizeHist",res)


