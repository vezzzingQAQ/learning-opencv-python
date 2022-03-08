'''
2021.2.2FromIvicxDS:openCV;E3B sobel算子
'''
'''
A=
a   b   c
d   e   f
g   h   i
Gx=
-1  0   1
-2  0   2   *A
-1  0   1
Gy=
-1  -2  -1
0   0   0   *A
1   2   1
输出边界信息
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

img=cv2.imread("image/kernel2.jpg",cv2.IMREAD_GRAYSCALE)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)#水平方向轮廓
#sobel(img,图像的深度,水平，竖直方向,算子的大小)

sobelx=cv2.convertScaleAbs(sobelx)
#绝对值让负数转换，得到轮廓的整体信息

sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)#竖直方向轮廓
#sobel(img,图像的深度,水平，竖直方向,算子的大小)

sobely=cv2.convertScaleAbs(sobely)
#绝对值让负数转换，得到轮廓的整体信息

sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)#按照权重相加xy

res=numpy.hstack((sobelx,sobely,sobelxy))
showPicture("",res)