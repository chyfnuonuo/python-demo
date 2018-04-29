#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/4/28'
__contact__ = 'chengyoufu@gmail.com'
"""


def trim(strin):
	ltmp = strin[:]
	for c in strin:
		if c == ' ':
			ltmp = ltmp[1:]
		else:
			break
	strin = ltmp[:]
	if len(strin) == 0:
		return strin
	list_temp = list(reversed(strin))
	ltmp = list_temp[:]
	for c in list_temp:
		if c == ' ':
			ltmp.remove(c)
		else:
			break
	ltmp.reverse()
	strin = ''.join(ltmp)
	return strin


def trip(s):
	while len(s) > 0:
		if s[0] == " ":
			s = s[1:]
		elif s[-1] == " ":
			s = s[:-1]
		else:
			break
	return s


if trip('hello  ') != 'hello':
	print('测试失败!')
elif trip('  hello') != 'hello':
	print('测试失败!')
elif trip('  hello  ') != 'hello':
	print('测试失败!')
elif trip('  hello  world  ') != 'hello  world':
	print('测试失败!')
elif trip('') != '':
	print('测试失败!')
elif trip('    ') != '':
	print('测试失败!')
else:
	print('测试成功!')
