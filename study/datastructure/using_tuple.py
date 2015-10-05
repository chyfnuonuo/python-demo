#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: using_tuple.py
@time: 2015/10/1 21:26
"""

zoo = ('wolf', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('mankey', 'dolphin', zoo)
print('Number of animals in new zoo are',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Animals brought from old zoo are',new_zoo[2])
print('Last animal brount from old zoo is',new_zoo[2][2])



