#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: using_file.py
@time: 2015/10/4 20:46
"""

poem='''\
Programming is fun
When the work  is done
if you wanna make your work also fun:
        use python!
'''


f=open('poem.txt','w')
f.write(poem)
f.close()
f=open('poem.txt','r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()

f=open('poem1.txt','w')
f.close()