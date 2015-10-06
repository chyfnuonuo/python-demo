#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: iterable.py
@time: 2015/10/6 14:20
"""
import collections

print(isinstance([],collections.Iterable))

print([x for x in range(10)])

l =list(x for x in range(10))
print(l)
isinstance((x for x in range(10)),collections.Iterator)
