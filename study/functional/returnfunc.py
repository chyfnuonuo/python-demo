#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: returnfunc.py
@time: 2015/10/10 20:44
"""


def func():
    pass


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def count():
    fs = []

    def f(j):
        def g():
            return j * j

        return g

    for i in range(1, 4):
        fs.append(f(i))  # f(i)需要返回一个函数
    return fs


f1, f2, f3 = count()

print(f1(), f2(), f3())


def createCounter():
    def num():
        m = 1
        while True:
            yield m
            m = m + 1

    n = num()

    def counter():
        return next(n)

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
