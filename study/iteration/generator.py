#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: generator.py
@time: 2015/10/5 22:46
"""

g=(x * x for x in range(10))
for gg in g:
    print(gg)

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'done'

f=fib(6)
for ff in f:
    print(ff)

def triangles(max):
    n =0
    a=1
