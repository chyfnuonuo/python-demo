#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: HigherOrderFunction.py
@time: 2015/10/6 14:27
"""


def func(x, y, f):
    return f(x) + f(y)


print(func(-5, 6, abs))
