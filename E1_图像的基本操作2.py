'''
2021.1.28FromIvicxDS:openCV;E1图像的基本操作
'''
'''
1.图像加边框
'''
import cv2#读取格式为BGR

def showPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/P1.jpg")

#给图像加边框
top_size,bottom_size,left_size,right_size=(70,70,70,70)

replicate=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,
                             borderType=cv2.BORDER_REPLICATE)
showPicture("replicate",replicate)#复制边缘像素

reflect=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,
                             borderType=cv2.BORDER_REFLECT)
showPicture("reflect",reflect)#镜面

reflect101=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,
                             borderType=cv2.BORDER_REFLECT_101)
showPicture("reflect101",reflect101)

warp=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,
                             borderType=cv2.BORDER_WRAP)
showPicture("warp",warp)

constant=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,
                             borderType=cv2.BORDER_CONSTANT,value=(200,200,100))
showPicture("constant",constant)