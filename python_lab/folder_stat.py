# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:15:07 2021

@author: Zandra
"""

import os
import sys

totalSize = 0
fileNum = 0
dirNum = 0

def visitDir(path):
    global totalSize
    global fileNum
    global dirNum
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum = fileNum+1                              #统计文件数量
            totalSize = totalSize+os.path.getsize(sub_path)  #统计文件总大小
        elif os.path.isdir(sub_path):
            dirNum = dirNum+1                                #统计文件夹数量
            visitDir(sub_path)                               #递归遍历子文件夹

def main(path):
    if not os.path.isdir(path):
        print('Error:"', path, '" is not a directory or does not exist.')
        #return
        sys.exit()
        #quit()
    visitDir(path)

def sizeConvert(size):                                   #单位换算
    K, M, G = 1024, 1024**2, 1024**3
    if size >= G:
        return str(size/G)+'G Bytes'
    elif size >= M:
        return str(size/M)+'M Bytes'
    elif size >= K:
        return str(size/K)+'K Bytes'
    else:
        return str(size)+'Bytes'

def output(path):
    print('The total size of '+path+' is:'+sizeConvert(totalSize)
          +'('+str(totalSize)+' Bytes)')
    print('The total number of files in '+path+' is:',fileNum)
    print('The total number of directories in '+path+' is:',dirNum)

if __name__=='__main__':
    path = r'C:\Users\Zandra\Desktop\python_labs\python\python_lab\tmp1'
    main(path)
    output(path)
