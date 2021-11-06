import time
import cv2
import datetime


def time_name():
    now = datetime.datetime.now()
    str_ymd = str(now.year)+"_"+str(now.month)+"_"+str(now.day)
    str_hm = str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)
    str_name = str_ymd+"-"+str_hm
    print (str_name)
    return str_name


def photo():
    try:
        camera = cv2.VideoCapture(0)
        # cv2.isOpened() 判断方法由于版本原因无法使用 此处略过
        if True:
            a = time_name()
            img_name = "/home/pi/Desktop/photos/" + a + ".jpg"
            camera.set(4, 1920)  # wide, high, fps
            camera.set(5, 1080)
            camera.set(6, 24)
            ret, frame = camera.read()
            cv2.imshow("test", frame)
            time.sleep(0.5)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
        camera.release()
        cv2.destroyAllWindows()
        return
    except(Exception):
        tick = time.time()
        print("STH is Wrong at " + str(tick))
