#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: func_key_var.py
@time: 2015/10/5 21:52
"""


def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

print(person('Michael',30))
print(person('Bob',30,city='Beijing'))
print(person('Adam',22,gender='M',job='Engineer'))

extra = {'city':'Beijing','job':'Engineer'}
print(person('Jack',24,**extra))

def personkey(name,age,*,city,job):
    print('name:',name,'age:',age,'city:',city,'job:',job)

print()