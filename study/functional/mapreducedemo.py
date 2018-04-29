# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/4/29'
__contact__ = 'chengyoufu@gmail.com'
"""
from functools import reduce


def prod(L):
	return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
	print('测试成功!')
else:
	print('测试失败!')


def normalize(name):
	return name[:1].upper() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def str2float(s):
	return reduce(lambda x, y: x * 10 + y, map(int, s.split('.')[0])) + reduce(lambda x, y: x / 10 + y,
	                                                                           list(map(int, s.split('.')[1]))[
	                                                                           ::-1]) / 10


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
	print('测试成功!')
else:
	print('测试失败!')
