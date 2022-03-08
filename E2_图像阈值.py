'''
2021.1.29FromIvicxDS:openCV;E2阈值函数
'''
'''
5种阈值处理
'''
import cv2#读取格式为BGR

def showPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/P1.jpg",cv2.IMREAD_GRAYSCALE)
#图像，阈值，max
#有两个返回值，一般只用第二个
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)#>127->255,<127->0
ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#1的反转黑白颠倒
ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)#设置截断值>127->127else不变
ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#设置截断值>127不变else->0
ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
showPicture("Original Picture",img)
showPicture("THRESH_BINARY",thresh1)
showPicture("THRESH_BINARY_INV",thresh2)
showPicture("THRESH_BINARY_INV",thresh3)
showPicture("THRESH_BINARY_INV",thresh4)
showPicture("THRESH_BINARY_INV",thresh5)