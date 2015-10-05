#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: list_comprehensions.py
@time: 2015/10/5 22:27
"""
import os
print(list(range(1, 11)))

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m+n for m in 'ABC' for n in 'CVB'])

print([d for d in os.listdir('..')])

