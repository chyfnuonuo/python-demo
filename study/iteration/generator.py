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

def triangles():
    n=1
    list_a=[1]
    while True:
        list_b=[]
        if n==1:
           list_b=list_a=[1]
        elif n==2:
            list_a=list_b=[1,1]
        else:
            for i in range(n):
                if i==0 or i==n-1:
                    list_b.append(1)
                else:
                    list_b.append(list_a[i-1]+list_a[i])
        yield list_b
        list_a=list_b
        n=n+1


def triangles2():
     L = [1]
     yield(L)
     L = [1,1]
     yield(L)
     while True:
        L = [1] + [L[ i ] + L[i + 1] for i in range(len(L) - 1)] + [1]
        yield L

n=0
for t in triangles2():
    print(t)
    n=n+1
    if (n==10):
        break