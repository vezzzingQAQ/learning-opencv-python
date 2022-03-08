'''
2021.1.29FromIvicxDS:openCV;E2图像形态处理：腐蚀操作1
'''
'''
1   1   1
1   0   1
0   0   0
->
1   1   1
1   1   1
1   1   1   
框内有黑色则改为全黑
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

img=cv2.imread("image/kernel.jpg")
showPicture("originalPicture",img)

#腐蚀操作*****************************
kernel=numpy.ones((3,3),numpy.uint8)
erosion=cv2.erode(img,kernel,iterations=1)
showPicture("eroded",erosion)

dear=cv2.imread("image/kernel2.jpg")
erosion1=cv2.erode(dear,kernel,iterations=1)
erosion2=cv2.erode(dear,kernel,iterations=3)
erosion3=cv2.erode(dear,kernel,iterations=5)
erosion4=cv2.erode(dear,kernel,iterations=7)
erosion5=cv2.erode(dear,kernel,iterations=9)

res1=numpy.hstack((dear,erosion1,erosion2))
res2=numpy.hstack((erosion3,erosion4,erosion5))
res=numpy.vstack((res1,res2))

showPicture("erodedList",res)