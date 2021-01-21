# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:09:42 2021

@author: chunxia
@package: settings
@module circles
"""

import math
Radis = 100

def area(R=Radis):
    return R*R*math.pi

if __name__ == "__main__":
    print(area(Radis))

