#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: func_paratest.py
@time: 2015/10/3 21:03
"""

def power(x):
    return  x*x

def power(x,n=2):
    s = 1
    while n >0:
        n-=1
        s=s*x
    return s


def add_end(L=None):#默认参数必须指向不变对象
    if L is None:
       L = []

    L.append('END')
    return L

L1=add_end([1,2,3])
print(L1)

L2=add_end(['a','b','c'])
print(L2)

L3=add_end()
print(L3)

L4=add_end()
print(L4)
