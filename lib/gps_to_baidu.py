# coding=utf-8
from gpsGet import gps_inof
import requests
import time


def get_baidu():
    info = gps_inof()
    ak = "jrgjikUuzrXcNKdStXPbAhbv0ZOKNfmz"
    lat = str(info[1][0])
    lng = str(info[1][1])
    url = "http://api.map.baidu.com/geoconv/v1/?coords=" + lat + "," + lng + "&from=1&to=5&ak=" + ak
    print(url)
    response = requests.get(url)
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        json_str = response.json()
        print(json_str['result'][0]['x'])  # type: #class 'list' #<class 'dict'>
        print(json_str['result'][0]['y'])
        baidu_lng = json_str['result'][0]['x']
        baidu_lat = json_str['result'][0]['y']
    ticks = time.time()
    arr = [ticks,baidu_lat,baidu_lng]
    return arr


def get_origin():
    info = gps_inof()
    lat = info[1][0]
    lng = info[1][1]
    ticks = time.time()
    arr = [ticks, lng, lat]
    return arr