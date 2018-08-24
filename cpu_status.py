#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

def get_cpu_temp():
    '''获取CPU温度，单位：摄氏度'''
    return os.popen('vcgencmd measure_temp').read().strip()[len('temp='):-len("'C")] + "°C"

def get_cpu_used():
    '''获取CPU使用率'''
    return os.popen("vmstat | sed -n '3p' | awk '{print 100 - $15}'").read().strip() + "%"

while True:
    print('使用率：%s\t 温度：%s' % (get_cpu_used(), get_cpu_temp()))
    time.sleep(1)
