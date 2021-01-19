# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 15:37:12 2021

@author: Zandra
"""

words = ('测试',
         '非法',
         '暴力',
        '黄瓜')
text ='这句话里有非法内容'

text = input('请输入检查内容：')

# check legal
for word in words:
    if word in text:
        print('非法')
        break
else: # else of for loop
    print('正常')

for word in words:
    if word in text:
        text=text.replace(word,'**')
        #break

print(text)