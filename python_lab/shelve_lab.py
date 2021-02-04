# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:40:22 2021

@author: Zandra
"""


import shelve
zhangsan = {'age':38, 'sex':'Male', 'address':'SDIBT'}
lisi = {'age':40, 'sex':'Male', 'qq':'1234567', 'tel':'7654321'}
with shelve.open('shelve_test.dat') as fp:
    fp['zhangsan'] = zhangsan      # 像操作字典一样把数据写入文件
    fp['lisi'] = lisi
    for i in range(5):
        fp[str(i)] = str(i)*3

with shelve.open('shelve_test.dat') as fp:
    print(fp['zhangsan'])                 #读取并显示文件内容
    print(fp['zhangsan']['age'])
    print(fp['lisi']['qq'])
    print(fp['3'])
    print("---fp.items---")
    for itm in fp.items():
        print(itm)