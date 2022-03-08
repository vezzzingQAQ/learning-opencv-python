'''
2021.2.1FromIvicxDS:openCV;E7：数字识别
'''
'''
素材列表:
0 1 2 3 4 5 6 7 8 9

-----------------------
this is a type of word
*****
4000 1234 5678 4020
-----------------------

-----------------------
2312222
##############

4213 2333 1232 2342
-----------------------

-----------------------
this is a type of word
*****
2301 2310 0000 3332
-----------------------

-----------------------
2391 0012 2222 3321
-----------------------

-----------------------
5514 3333 2222 1111
-----------------------

-----------------------
1234 5678 9012 3456
-----------------------
'''
import cv2
import numpy
import E_myutils
def showPicture(name="",picture=None):
    #图像的显示,也可以显示多窗口
    cv2.imshow(name,picture)
    #在键盘中按任意键退出显示并向后执行语句
    #cv2.waitKey(1000)表示只显示1秒
    cv2.waitKey(0)
    cv2.destroyAllWindows()

accuracyX=0
accuracyY=0
resizedSize=(57,88)
upFloatValue=5

img=cv2.imread("image/E7/material.JPG")
#showPicture("material",img)#step1读取模板

ref=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#showPicture("gray",ref)#step2转灰度图

ref=cv2.threshold(ref,100,255,cv2.THRESH_BINARY)[1]#返回值有两个
#showPicture("tz",ref)#step3转为二值图

refCnts,hierachy=cv2.findContours(ref.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#RETR_EXTERNAL表示只检测外轮廓
#step4轮廓检测
cv2.drawContours(img,refCnts,-1,(0,255,255),1)
#showPicture("4",img)

refCnts=E_myutils.sort_contours(refCnts,method="left_to_right")[0]
#step5对轮廓按照从左到右排序

digits={}
for (i,c) in enumerate(refCnts):
    (x,y,w,h)=cv2.boundingRect(c)
    roi=ref[y:y+h,x:x+w]
    roi=cv2.resize(roi,resizedSize)
    digits[i]=roi
    #showPicture(picture=roi)
#step6将数字的方形区域与数字对应

rectKernel=cv2.getStructuringElement(cv2.MORPH_RECT,(9,3))
sqKernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#指定卷积核大小

img=cv2.imread("image/E7/2.JPG")
#showPicture(picture=img)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#showPicture(picture=gray_img)
#step1读取要识别的图，进行灰度处理

tophat_img=cv2.morphologyEx(gray_img,cv2.MORPH_TOPHAT,rectKernel)
#showPicture(picture=tophat_img)#step2滤除一些杂点，突出重点

gradX=cv2.Sobel(tophat_img,ddepth=cv2.CV_32F,dx=1,dy=0,ksize=-1)
gradX=numpy.absolute(gradX)
(minVal,maxVal)=(numpy.min(gradX),numpy.max(gradX))
gradX=(255*((gradX-maxVal)/(maxVal-minVal)))
gradX=gradX.astype("uint8")
#showPicture(picture=gradX)

gradX=cv2.morphologyEx(gradX,cv2.MORPH_CLOSE,rectKernel)
#step3执行闭操作：先膨胀再腐蚀【有些细节膨胀后腐蚀不掉】，是图像更像一块一块的
#showPicture(picture=gradX)

thresh=cv2.threshold(gradX,0,255,
                     cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
#step4自动按照图像特征二值化图像【0,255】的原因cv2.THRESH_OTSU
#showPicture(picture=thresh)

thresh=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,sqKernel)
#step5再进行一次闭操作，进一步去除图像中的空点
#showPicture(picture=thresh)

threshCnts,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)
#step6寻找轮廓

cnts=threshCnts
cur_img=img.copy()
cv2.drawContours(cur_img,cnts,-1,(0,255,255),1)
#showPicture(picture=cur_img)

locations=[]
for (i,c) in enumerate(cnts):
    (x,y,w,h)=cv2.boundingRect(c)
    ar=w/float(h)#计算长宽比
    if ar>2 and ar<4:
        locations.append((x,y,w,h))
#step7根据长宽比判断哪些轮廓要保留

locations=sorted(locations,key=lambda x:x[0])
#step8将这几个大轮廓从左到右排序

output=[]
for(i,(gX,gY,gW,gH)) in enumerate(locations):
    groupOutput=[]
    group=gray_img[gY-accuracyY:gY+gH+accuracyY,gX-accuracyX:gX+gW+accuracyX]
    #showPicture(picture=group)
    #提取出每个组
    group=cv2.threshold(group,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
    #showPicture(picture=group)
    #二值化
    digitCnts,hierarchy=cv2.findContours(group.copy(),cv2.RETR_EXTERNAL
                                         ,cv2.CHAIN_APPROX_SIMPLE)
    #计算轮廓
    digitCnts=E_myutils.sort_contours(digitCnts,
                                      method="left_to_right")[0]
    #轮廓排序
    for i in digitCnts:
        (x,y,w,h)=cv2.boundingRect(i)
        roi=group[y:y+h,x:x+w]
        roi=cv2.resize(roi,resizedSize)
        #showPicture(picture=roi)
        scores=[]
        for(digit,digitROI) in digits.items():#匹配
            result=cv2.matchTemplate(roi,digitROI,
                                     cv2.TM_CCOEFF_NORMED)
            score=cv2.minMaxLoc(result)[1]
            scores.append(score)
        groupOutput.append(str(numpy.argmax(scores)))
        print(scores)
    cv2.rectangle(img,(gX-accuracyX,gY-accuracyY),
                  (gX+gW+accuracyX,gY+gH+accuracyY),(0,255,255),1)
    cv2.putText(img,"".join(groupOutput),
                (gX,gY-upFloatValue),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    output.extend(groupOutput)#一组一组算
print(output)
showPicture(picture=img)





