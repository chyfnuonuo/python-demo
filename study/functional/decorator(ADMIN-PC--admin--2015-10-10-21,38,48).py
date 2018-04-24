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
    """testset

    :param func: etst
    :return: setst
    """
    def wrapper(a,b):
        starttime = time.time()
        func(a,b)
        endtime = time.time()
        msecs = (endtime - starttime) * 1000
        print(">>elapesd time:%f ms"%msecs)

    return  wrapper

@deco
def myfunc(a,b):
    print('start myfunc')
    time.sleep(0.6)
    print('result is %d'%(a+b))
    print('end myfunc')


myfunc(3,8)
