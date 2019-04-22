#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time

def get_cpu_temp():
    '''获取CPU温度，单位：摄氏度'''
    return os.popen('vcgencmd measure_temp').read().strip()[len('temp='):-len("'C")]

def get_cpu_used():
    '''获取CPU使用率'''
    s = os.popen("top -n 2 -b").read().strip()
    return re.search(r"Cpu\(s\)[\w\W]*Cpu\(s\): ([\d\.]*) us", s).group(1)

while True:
    print('使用率：%s%%\t 温度：%s°C' % (get_cpu_used(), get_cpu_temp()))
    # time.sleep(1)
