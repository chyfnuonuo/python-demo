#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/4/29'
__contact__ = 'chengyoufu@gmail.com'
"""
import functools


def log(param=""):
	if callable(param):
		def wrapper(*args, **kwargs):
			print("begin call")
			reasult = param(*args, **kwargs)
			print("end call")
			return reasult

		return wrapper
	elif isinstance(param, str):
		def decorator(func):
			def wrapper(*args, **kwargs):
				print("begin call " + param)
				reasult = func(*args, **kwargs)
				print("end call " + param)
				return reasult

			return wrapper

		return decorator
	else:
		raise TypeError


@log
def f1():
	print("test")


@log("haha")
def f2():
	print("haha")


f1()
f2()
