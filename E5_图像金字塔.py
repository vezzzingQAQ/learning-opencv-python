'''
2021.1.30FromIvicxDS:openCV;E5图像形态处理：图像金字塔
'''
'''
高斯金字塔:************************************************
1.向下采样法【向下为图像缩小的方向(图中箭头)】>>>>>>>>>>>>>>>>>>>>
 /__\   ↑
/____\  ↑
step1.将Gi与高斯内核卷积【高斯滤波】
高斯内核:
1   4   6   4   1
4   16  24  16  4
6   24  36  24  6   1/16
4   16  24  16  4
1   4   6   4   1
step2.去除所有偶数行列
2.向上采样法>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 /__\   ↓
/____\  ↓
step1.图像每个方向上扩大为原来的两倍，新增的行列以0填充
10  30
55  23
↓
10  0   30  0
0   0   0   0
55  0   23  0
0   0   0   0
step2.使用与先前同样的内核(x4)与放大后的图像卷积。获得近似值
拉普拉斯金字塔***********************************************
Li【处理后的结果】=Gi【原图】-pyrUp(pyrDown(Gi))
step1.低通滤波
step2.缩小尺寸
step3.放大尺寸
step4.图像相减【比较出差异】
'''
import cv2#读取格式为BGR

def showPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/x1.jpg")#高斯金字塔>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print(img.shape)
downPicture=cv2.pyrDown(img)
print(downPicture.shape)
showPicture("pyrUp",downPicture)
#pyrUp用法相同

down=cv2.pyrDown(img)
down_up=cv2.pyrUp(down)
lupls=img-down_up
showPicture("LplsPyr",lupls)
