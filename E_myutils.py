'''
2021.2.1:轮廓排序
'''
import cv2

def sort_contours(cnts,method="left_to_right"):
    boundingBoxes=[cv2.boundingRect(i) for i in cnts]
    #做轮廓的外接矩形，求左上角坐标排序
    #返回一个元组(x,y,h,w)
    '''
    print(str(boundingBoxes))

    x_first=[boundingBoxes[i][0] for i in range(len(cnts))]
    y_first=[boundingBoxes[i][1] for i in range(len(cnts))]
    result=[]

    if method=="left_to_right":
        result=x_first.sort()
    elif method=="right_to_left":
        result=x_first.sort(reverse=True)
    elif method=="top_to_bottom":
        result=y_first.sort()
    elif method=="bottom_to_top":
        result=y_first.sort(reverse=True)
    else:
        print("ERROR>>")
        return
    return cnts,result
    '''
    reverse=False
    i=0
    if method=="right_to_left" or method=="bottom_to_top":
        reverse=True
    if method=="top_to_bottom" or method=="bottom_to_top":
        i=1
    (cnts,boundingBoxes)=zip(*sorted(zip(cnts,boundingBoxes),
                                     key=lambda b:b[1][i],reverse=reverse))
    return cnts,boundingBoxes

