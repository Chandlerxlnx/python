# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 10:06:25 2021

@author: Zandra
"""

'''
 input() output is string!
'''
a = input("请输入a:")
b = input("请输入b:")

if a<b:
    print(a+"<"+b)
elif a>b:
    print(a+'>'+b)
else:
    print(a+'=='+b)
    
print(type(a))


x= input('Input two number:')
a,b = map(int,x.split())
# a,b are int now.
if a<b:
    print(a,"<",b)
elif a>b:
    print(a,'>',b)
else:
    print(a,'==',b)
    
print(type(a))