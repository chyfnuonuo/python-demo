#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: using_dict.py
@time: 2015/10/1 21:46
"""

ab={'key1':'value1','key2':'value2','key3':'value3'}

print('key1 value is %s'%ab['key1'])

ab['key4']='value4'
del ab['key1']
print('There are %d elm in the map\n'%len(ab))

for key,value in ab.items():
    print('%s at %s'%(key,value))
for key, value in ab.items():
    pass
    
if 'key2' in ab:
    print('test')

t=set([1,2,3])
t.add((1,[2,3]))
print(t)
