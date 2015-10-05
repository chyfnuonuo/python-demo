#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: using_list.py
@time: 2015/10/1 21:12
"""

shoplist = ['apple','mango','carot','banana']

print('i have',len(shoplist),'items to purchase')

print('These items are:')
# Notice the comma at end of the line

for item in shoplist:
    print(item,),

print('\nI also hava to buy rice')
shoplist.append('rice')
print('my shopping list is now',shoplist)

print('I will sort my list now')

shoplist.sort()

print('Sorted shopping list is',shoplist)

print('The first item I will buy is',shoplist[0])

olditem=shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping List is now',shoplist)

booklist = ['book1','book2','book3']
shoplist.append(booklist)
print(shoplist)#列表中的列表不会失去省份