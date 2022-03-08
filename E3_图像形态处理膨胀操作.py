'''
2021.1.29FromIvicxDS:openCV;E2图像形态处理：膨胀操作1
'''
'''
1   0   1
1   0   0
0   0   0
->
0   0   0
0   0   0
0   0   0
框内有白色则改为全白
先腐蚀再膨胀可以去除杂边
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
erosion=cv2.erode(img,kernel,iterations=3)
showPicture("eroded",erosion)

#膨胀操作*****************************
process=cv2.dilate(erosion,kernel,iterations=3)
showPicture("returned",process)

res=numpy.hstack((img,erosion,process))
showPicture("totalProcess",res)

'''
开运算：先腐蚀再膨胀
闭运算：先膨胀再腐蚀
'''