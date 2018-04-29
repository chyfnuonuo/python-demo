#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/4/28'
__contact__ = 'chengyoufu@gmail.com'
"""


def findMinAndMax(L):
	if len(L) == 0 or not isinstance(L, list):
		return (None, None)
	else:
		maxtemp = L[0]
		mintemp = L[0]

	for num in L:
		if num > maxtemp:
			maxtemp = num
		if num < mintemp:
			mintemp = num
	return (mintemp, maxtemp)


if findMinAndMax([]) != (None, None):
	print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
	print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
	print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
	print('测试失败!')
else:
	print('测试成功!')
