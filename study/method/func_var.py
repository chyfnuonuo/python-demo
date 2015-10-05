#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: func_var.py
@time: 2015/10/5 21:47
"""


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return  sum

num = calc(1,2,3,4,5)
print(num)

nums = [1,2,3,4,5]

numss=calc(*nums)
print(numss)


