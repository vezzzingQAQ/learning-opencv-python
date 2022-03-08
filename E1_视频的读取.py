'''
2021.1.28FromIvicxDS:openCV;E1视频的读取
'''
'''
2.视频的读取
'''
import cv2#读取格式为BGR

vc=cv2.VideoCapture("video/1.mp4")

#检查打开是否正常
if vc.isOpened():
    open,frame=vc.read()#执行vc.read()往后读一帧
else:
    open=False

#遍历所有帧
while True:
    ret,frame=vc.read()
    if frame is None:#为空（播放完了）
        break
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#转成灰度图
        cv2.imshow("result",gray)
        if cv2.waitKey(10) & 0xFF==27:#设置帧率，27表示按Esc退出
            break
vc.release()
cv2.destroyAllWindows()