# -*- coding: utf-8 -*-
# 异步进程传输文件并在传输后终止
# 标准以太网帧长度上限为1518字节>256
# 加入哈希校验
import asyncio
import socket
import os
import struct
import sys
import hashlib

# hostname = str('111.230.137.99')
hostname = str('localhost')
port = int('10010')
file_path = str('test/')


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hostname, port))
    except socket.error as err:
        print(err)
        sys.exit(1)
    print(s.recv(1024))
    files = os.listdir(file_path)
    for file in files:
        filepath = os.path.join(file_path, file)
        if os.path.isfile(filepath):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            file_info_size = struct.calcsize('256sl')
            print(file_info_size)
            # 定义文件头信息，包含文件名和文件大小
            file_head = struct.pack('256sl', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
            # 发送文件名称与文件大小
            s.send(file_head)
            # 将传输文件以二进制的形式分多次上传至服务器
            fp = open(filepath, 'rb')
            while True:
                data = fp.read(2048)
                if not data:
                    print('{0} file send over...'.format(os.path.basename(filepath)))
                    break
                s.send(data)
            fp.close()
            data_m5 = open(filepath, 'rb')
            data_md5 = data_m5.read()
            file_md5 = hashlib.md5(data_md5).hexdigest()
            print(file_md5)
            # 解决粘包问题
            # fm = struct.pack('256s1',file_md5)
            s.send(file_md5.encode('utf-8'))
            fin = s.recv(1024)
            if (fin.decode() == 'ERROR'):
                print('文件：' + filepath + '传输过程出错，未通过md5校验，请重新开始本线程传输')
            else:
                if(fin.decode() == 'SUCCESS'):
                    print('文件：' + filepath + '通过md5校验')
    # os.remove(file_path)
    s.close()


if __name__ == '__main__':
    socket_client()