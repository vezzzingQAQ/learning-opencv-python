'''
2021.1.31FromIvicxDS:openCV;E6：傅里叶变换和滤波器
'''
'''
高频：变化剧烈的灰度值【边界】
低频：
滤波：
    低通滤波器：只保留低频，会使图像模糊
    高通滤波器：只保留高频，会使图像细节增强
openCV操作
    cv2.dft(),cv2.idft正逆操作，图像要转换为np.float32格式
    默认结果低频在左上角，通过shift变换拉到中心位置
    cv2.dft()的返回结果是复数，要转换为图像格式才能展示(0,255)
'''

import cv2#读取格式为BGR
import numpy
from matplotlib import pyplot as plt

img=cv2.imread("image/x1.jpg",0)

img_float32=numpy.float32(img)

dft=cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=numpy.fft.fftshift(dft)

magnitude_spectrum=20*numpy.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121)
plt.imshow(img,cmap="gray")
plt.title("input image")
plt.xticks(())
plt.yticks(())

plt.subplot(122)
plt.imshow(magnitude_spectrum,cmap="gray")
plt.title("magnitude_spectrum")
plt.xticks(())
plt.yticks(())

plt.show()





