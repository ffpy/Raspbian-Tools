#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'获取树莓派的状态'

_author_ = 'FFPY'

import os

def get_cpu_temp():
    '''获取CPU温度，单位：摄氏度'''
    return os.popen('vcgencmd measure_temp').read().strip()[len('temp='):-len("'C")] + "°C"

def get_cpu_used():
    '''获取CPU使用率'''
    return os.popen("vmstat | sed -n '3p' | awk '{print 100 - $15}'").read().strip() + "%"

def get_ram_total():
    '''获取总RAM'''
    return os.popen("free -h | sed -n '2p' | awk '{print $2}'").read().strip()

def get_ram_used():
    '''获取已用RAM'''
    return os.popen("free -h | sed -n '2p' | awk '{print $3}'").read().strip()

def get_ram_used_percent():
    '''获取已用RAM百分比'''
    return os.popen("free -h | sed -n '2p' | awk '{percent=$3*100/$2} END {printf \"%d%%\\n\", percent}'").read().strip()

def get_ram_free():
    '''获取可用RAM'''
    return os.popen("free -h | sed -n '2p' | awk '{ print $4}'").read().strip()

def get_ip_addr():
    '''获取IP地址'''
    return os.popen("ifconfig | grep inet | awk '{print $2}' | grep -v '127.0.0.1' | egrep '([0-9]{1,4}\.){3}[0-9]{1,4}'").read().strip()

def get_disk_space_status():
    '''获取磁盘空间状态'''
    return os.popen("df -h | tail +2 | grep ^/dev | awk '{printf \"%s\\t%s\\t%s\\t%s\\t%s\\n\", $1,$6,$3,$4,$5}'").read().strip()

print('CPU\n使用率：%s\n温度：%s\n' % (get_cpu_used(), get_cpu_temp()))
print('内存\n总计\t已用\t可用\t已用百分比\n%s\t%s\t%s\t%s\n' % (get_ram_total(), get_ram_used(), get_ram_free(), get_ram_used_percent()))
print('IP地址\n%s\n' % get_ip_addr())
print('磁盘\n文件系统\t挂载点\t已用\t可用\t已用百分比\n%s' % get_disk_space_status())
