#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""Here端"""

import socket
import time

PORT = 6666     # 监听端口
NAME = 'Raspbian'   # Here端名字

# 创建广播接收套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 绑定端口
s.bind(('', PORT))

# 等待接收数据
while True:
    data, address = s.recvfrom(65535)
    # 发送数据
    s.sendto(NAME.encode('utf-8'), address)

