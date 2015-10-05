#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: class_init.py
@time: 2015/10/3 22:37
"""


class person():
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print('hello,my name is', self.name)


p = person('leo')
p.sayhi()

if __name__ == '__main__':
    print('hello')
