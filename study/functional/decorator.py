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
import functools


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)
        print(">>elapesd time:%f ms" % msecs)
        return result
    return wrapper


@metric
def myfunc(a, b):
    print('start myfunc')
    time.sleep(0.6)
    print('result is %d' % (a + b))
    print('end myfunc')


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
