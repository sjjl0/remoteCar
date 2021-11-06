#!/home/pi/server
# coding=utf-8
import websocket
import lib.basicMovement as move
import lib.pictureGet as photo
import lib.gpsGet as gps


# 初始参数
speed = 50
moveTime = 2

# webSocket的处理函数
def on_message(self, message):
    global speed
    global moveTime
    default = True
    # 简单的重新验证
    if "success" in message:
        ws.send('get')
        default = False
        return

    if "fail" in message:
        ws.send('admin')
        default = False
        return

    if "up" in message:
        m = message.split(" ")
        if len(m) <= 1:
            move.t_up(speed,moveTime)
        else:
            move.t_up(speed,int(m[1]))
        ws.send('ok')
        default = False
        return

    if "down" in message:
        m = message.split(" ")
        if len(m) <= 1:
            move.t_down(speed, moveTime)
        else:
            move.t_down(speed, int(m[1]))
        ws.send('ok')
        default = False
        return

    if "left" in message:
        m = message.split(" ")
        if len(m) <= 1:
            move.t_left(speed, moveTime)
        else:
            move.t_left(speed, int(m[1]))
        ws.send('ok')
        default = False
        return

    if "right" in message:
        m = message.split(" ")
        if len(m) <= 1:
            move.t_right(speed, moveTime)
        else:
            move.t_right(speed, int(m[1]))
        ws.send('ok')
        default = False
        return

    if "stop" in message:
        m = message.split(" ")
        if len(m) <= 1:
            move.t_stop(2)
        else:
            move.t_stop(int(m[1]))
        ws.send('ok')
        default = False
        return

    if "changeSpeed" in message:
        m = message.split(" ")
        speed = int(m[1])
        ws.send('ok')
        default = False
        return

    if "photo" in message:
        photo.photo()
        ws.send('ok')
        default = False
        return

    if "getGps" in message:
        GPSInfo = gps.gps_inof()
        ws.send(str(GPSInfo))
        default = False
        return

    if default:
        print(message)
        ws.send('not an effective command')
        return


def on_error(self, error):
    print(error)


def on_close(self):
    print("ConnectionClosed...")


def on_open(self):
    ws.send("admin")
    print("ConnectionStarted...")


if __name__ == '__main__':
    url = "ws://localhost:10086"
    while True:
        try:
            websocket.enableTrace(True)
            ws = websocket.WebSocketApp(url,
                                        on_open=on_open,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)
            ws.run_forever()
        except Exception as e:
            print(e)
            continue
