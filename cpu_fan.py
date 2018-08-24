#!/usr/bin/env python3
# -*-coding: utf-8 -*-

'根据CPU温度自动控制风扇开关'

_author_ = 'FFPY'

CHANNEL = 11        # 控制引脚
OPEN_TEMP = 55      # 打开风扇的温度（度）
CLOSE_TEMP = 40     # 关闭风扇的温度（度）
CHECK_INTERVAL = 30 # 循环检测的间隔（秒）

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
        GPIO.output(CHANNEL, GPIO.HIGH)
    elif temp < CLOSE_TEMP: # 低于CLOSE_TEMP关风扇
        GPIO.output(CHANNEL, GPIO.LOW)

def loop():
    '''循环检测'''
    while True:
        check()
        time.sleep(CHECK_INTERVAL)   # 休眠CHECK_INTERVAL秒

init()
loop()
GPIO.cleanup()
