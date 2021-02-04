# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:12:40 2021

@author: chunxia
"""

width = 800
height = 600

# example shows that __main__ will not run during package importing

if __name__ == '__main__':
    print("height:",height)
    print("宽度：",width)
