#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: hanoi.py
@time: 2015/10/5 22:09
"""


def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)
        hanoi(1,x,y,z)
        hanoi(n-1,y,x,z)

hanoi(10,'x','y','z')

