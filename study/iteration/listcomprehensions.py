#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'cheng'
__mtime__ = '2018/4/28'
__contact__ = 'chengyoufu@gmail.com'
"""

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
