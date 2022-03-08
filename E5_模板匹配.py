'''
2021.1.30FromIvicxDS:openCV;E5图像形态处理：模板匹配
'''
'''
原图：AxB,模板axb->结果矩阵:(A-a+1)x(B-b+1)
匹配算法:
TM_SQDIFF:计算平方不同，值越小，越相关
TM_CCORR:计算相关性，值越大，越相关
TM_CCOEFF:计算相关系数，值越大，越相关
TM_SQDIFF_NORMED:计算归一化平方不同，越接近0，越相关#也是最大最小值
TM_CCORR_NORMED:计算归一化相关性，越接近1，越相关#也是最大最小值
TM_CCOEFF_NORMED:计算归一化相关系数，越接近1，越相关#也是最大最小值
'''
import cv2

def showPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/C2_1.jpg",0)#转为灰度图
imgOriginal=cv2.imread("image/C2_1.jpg")
template=cv2.imread("image/CM_1.jpg",0)
h,w=template.shape[:2]

showPicture("template",template)

res=cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)#定位左上角坐标，宽高为templte

img1=cv2.rectangle(imgOriginal,max_loc,(max_loc[0]+w,max_loc[1]+h),(0,255,0),2)

showPicture("matchResult",img1)
