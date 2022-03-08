'''
2021.1.28FromIvicxDS:openCV;E1图像的基本操作
'''
'''
图像的矩阵化
1.图像的读取
2.图像颜色矩阵的输出
3.图像的显示
4.图像的颜色通道拆分与输出
5.图像颜色通道的合并
6.彩图改为灰度图
'''
import cv2#读取格式为BGR
#图像的读取

def ShowPicture(name,picture):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread("image/P1.jpg")
print("<图片的像素值>")
print(img)

print("图片的hwc,3表示RGB彩色图")
print(img.shape)

ShowPicture("this is a window",img)#显示图像

#读取为灰度图像
img2=cv2.imread("image/P1.jpg",cv2.IMREAD_GRAYSCALE)

print("<图片的像素值>")
print(img2)

print("图片的hw,2表示灰度图")
print(img2.shape)

ShowPicture("this is a no-colored picture",img2)

#图像的保存
cv2.imwrite("P3.jpg",img2)

#读取图像大小
print("<图像的大小>")
print(img2.size)

#截取部分图像ROI
imgshow=img2[0:200,0:200]
ShowPicture("cutting picture",imgshow)

#颜色通道的提取
b,g,r=cv2.split(img)
print("<颜色通道提取>")
print("<B>*******************")
print(b)
print("B.shape=")
print(b.shape)
print("<G>*******************")
print(g)
print("G.shape=")
print(g.shape)
print("<R>*******************")
print(r)
print("R.shape=")
print(r.shape)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

#从颜色通道合成图像
img3=cv2.merge((b,g,r))
ShowPicture("an merged picture",img3)
print("合成后图像的shape值=")
print(img3.shape)

#只保留R通道
#BGR->[,,]三维数组切片->0，1，2
R_image=img3.copy()
R_image[:,:,0]=0
R_image[:,:,1]=0
ShowPicture("R",R_image)
