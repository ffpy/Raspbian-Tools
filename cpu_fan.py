#!/usr/bin/env python3
# -*-coding: utf-8 -*-

'根据CPU温度自动控制风扇开关'

_author_ = 'FFPY'

CHANNEL = 11        # 控制引脚
OPEN_TEMP = 60      # 打开风扇的温度（度）
CLOSE_TEMP = 55     # 关闭风扇的温度（度）
CLOSE_CHECK_INTERVAL = 20 # 关状态检测的间隔（秒）
OPEN_CHECK_INTERVAL = 600 # 开状态检测的间隔（秒）
isOpen = False # 是否为开状态

import os
import time
import RPi.GPIO as GPIO

def get_cpu_temp():
    '''获取CPU温度'''
    return float(os.popen('vcgencmd measure_temp').read().strip()[len('temp='):-len("'C")])

def init():
    '''初始化环境'''
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(CHANNEL, GPIO.OUT)

def check():
    '''检测温度并控制风扇'''
    temp = get_cpu_temp()
    if temp > OPEN_TEMP:    # 高于OPEN_TEMP开风扇
        isOpen = True
        GPIO.output(CHANNEL, GPIO.HIGH)
    elif temp <= CLOSE_TEMP: # 低于CLOSE_TEMP关风扇
        isOpen = False
        GPIO.output(CHANNEL, GPIO.LOW)

def loop():
    GPIO.output(CHANNEL, GPIO.LOW)
    '''循环检测'''
    while True:
        check()
        if isOpen:
            time.sleep(OPEN_CHECK_INTERVAL)
        else:
            time.sleep(CLOSE_CHECK_INTERVAL)

init()
loop()
GPIO.cleanup()
