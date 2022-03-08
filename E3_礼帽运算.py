'''
2021.1.29FromIvicxDS:openCV;E2图像形态处理：礼帽运算
'''
'''
对图像
开运算
原始图像-开运算结果->噪点信息
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
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
showPicture("tophat",tophat)