'''
2021.2.2FromIvicxDS:openCV;E3B Scharr和laplacian算子
'''
'''
Scharr算子:
Gx=
-3  0   3
-10 0   10  *A
-3  0   0
Gy=
-3  -10 -3
0   0   0   *A
3   10  3
相较于sobel算子对变化更敏感
laplacian算子:
G=
0   1   0
1   -4  1
0   1   0
【二阶导】
更敏感但容易受到噪点影响
'''
import cv2  # 读取格式为BGR
import numpy


def showPicture(name, picture):
    # 图像的显示,也可以显示多窗口
    cv2.imshow(name, picture)
    # 在键盘中按任意键退出显示并向后执行语句
    # cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("image/x1.jpg", cv2.IMREAD_GRAYSCALE)

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
sobely=cv2.convertScaleAbs(sobely)
sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

scharrx=cv2.Scharr(img,cv2.CV_64F,1,0)
scharry=cv2.Scharr(img,cv2.CV_64F,0,1)
scharrx=cv2.convertScaleAbs(scharrx)
scharry=cv2.convertScaleAbs(scharry)
scharrxy=cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

laplacian=cv2.Laplacian(img,cv2.CV_64F)
laplacian=cv2.convertScaleAbs(laplacian)

res=numpy.hstack((sobelxy,scharrxy,laplacian))
showPicture("",res)
