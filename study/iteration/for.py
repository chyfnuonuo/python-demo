#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: for.py
@time: 2015/10/5 22:16
"""
import collections
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)

for ch in 'ABCDF':
    print(ch)

for i,value in  enumerate(['a','b','c']):
    print(i,value)

for x,y in [(1,1),(2,4),(3,5)]:
    print(x,y)

print(isinstance('abc',collections.Iterable))