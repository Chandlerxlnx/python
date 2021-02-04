# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:11:42 2021

@author: Zandra
"""

import time

date = time.localtime()
print(date)
print(date.tm_mday)                      #获取当前日期时间
year, month, day = date[:3]
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year%400==0 or (year%4==0 and year%100!=0):   #判断是否为闰年
    day_month[1] = 29
if month==1:
    print(day)
else:
    print(sum(day_month[:month-1])+day)

