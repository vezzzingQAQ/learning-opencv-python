'''
2021.1.31FromIvicxDS:openCV;E6：直方图,直方图均衡化
'''
'''
灰度值->像素个数->概率->累计概率->根据函数映射后的灰度值->取整
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

img=cv2.imread("image/93401a6eb97e5b304361025f759006d.jpg",0)
equ=cv2.equalizeHist(img)
res=numpy.hstack((img,equ))

showPicture("equalizeHist",res)


