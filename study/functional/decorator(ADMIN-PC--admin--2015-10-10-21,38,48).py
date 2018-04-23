#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: decorator.py
@time: 2015/10/10 20:49
"""
import time





def deco(func):
    def wrapper(a,b):
        startTime=time.time()
        func(a,b)
        endTime=time.time()
        msecs=(endTime-startTime)*1000
        print(">>elapesd time:%f ms"%msecs)

    return  wrapper

@deco
def myfunc(a,b):
    print('start myfunc')
    time.sleep(0.6)
    print('result is %d'%(a+b))
    print('end myfunc')

myfunc(3,8)



