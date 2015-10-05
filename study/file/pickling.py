#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: pickling.py
@time: 2015/10/5 14:03
"""
import cPickle

shoplistfile = 'shoplist.data'
shoplist = ['apple','mando','caroot']

f=open(shoplistfile,'w')
cPickle