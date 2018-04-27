#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/4/27'
__contact__ = 'chengyoufu@gmail.com'
"""


def move(n, source, temp, dst):
	if n == 1:
		print(source, '->', dst)
	else:
		move(n - 1, source, dst, temp)
		move(1, source, temp, dst)
		move(n - 1, temp, source, dst)


move(3, 'source', 'temp', 'dst')
