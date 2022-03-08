'''
2021.1.31FromIvicxDS:openCV;E6：傅里叶变换和滤波器
'''
import cv2#读取格式为BGR
import numpy
from matplotlib import pyplot as plt

img=cv2.imread("image/x1.jpg",0)

img_float32=numpy.float32(img)

dft=cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=numpy.fft.fftshift(dft)

rows,cols=img.shape
crow,ccol=int(rows/2),int(cols/2)#确定中心位置

mask=numpy.zeros((rows,cols,2),numpy.uint8)#低通滤波【取中心正方形】
mask[crow-30:crow+30,ccol-30:ccol+30]=1

fshift=dft_shift*mask
f_ishift=numpy.fft.ifftshift(fshift)#逆运算一步步返回为图像
img_back=cv2.idft(f_ishift)
img_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121)#表格
plt.imshow(img,cmap="gray")
plt.title("input image")
plt.xticks(())
plt.yticks(())

plt.subplot(122)#表格
plt.imshow(img_back,cmap="gray")
plt.title("output image")
plt.xticks(())
plt.yticks(())

plt.show()
