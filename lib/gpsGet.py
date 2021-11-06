# coding=utf-8
#调用串口接收信息，调用一次函数获取一次GPS信息
import serial
import time
import math
from time import sleep

# 换成linux系统中GPS接收机对应的设备文件 /dev/ttyUSB1
deviceName = "/dev/ttyUSB0"

# 从串口GPS接收机选取可用最小终端
def gps_get():
    s = serial.Serial(deviceName, 9600)
    msg = ""
    arr = []
    while True:
        received_data = s.readline()
        if not received_data == "":
            msg = received_data.decode()
            arr = msg.split(",")
            # ['$GNRMC', '091900.000', 'V', '', '', '', '', '', '', '050521', '', '', 'M', 'V*28\r\n']
            if arr[0] == '$GNRMC':
                if arr[2] == "A":
                    print(arr)
                    break
        sleep(0.01)
    return arr

# 处理可用GPS信息，定位信息依靠串口数据，时间戳信息从本机获取
def gps_analysis():
    msg = gps_get()
    lat = float(msg[3])
    lng = float(msg[5])
    pos = [math.floor(lng/100),math.floor(lat/100)]
    pos = [pos[0]+(lng-pos[0]*100)/60, pos[1]+(lat-pos[1]*100)/60]
    print(pos)
    return pos


def gps_inof():
    ticks = time.time()
    pos = gps_analysis()
    arr = [ticks,pos]
    print(arr)
    return arr
