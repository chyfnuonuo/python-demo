#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: objvar.py
@time: 2015/10/3 22:32
"""


def func():
    pass


class person():
    '''Represents a person'''
    popluation = 0

    def __init__(self, name):
        '''Initializes the person's data'''
        self.name = name
        print('initializes person %s'%self.name)
        person.popluation+=1

    def __del__(self):
        '''I'm dying'''
        print('%s say bye'%self.name)
        person.popluation-=1
        if person.popluation==1:
            print("I'm the last one")
        else:
            print('There are still %d people alive'%person.popluation)

    def sayhi(self):
        ''' Greeting by the person
        Really that's all it does'''
        print('hi,my name is %s'%self.name)

    def howmany(self):
        '''Prints the current population

        :return error:
        '''
        if person.popluation==1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.'%self.popluation)

p=person('leo')
p.sayhi()
p.howmany()

c = person('c')
c.sayhi()
c.howmany()

print(person.__doc__)
print(p.sayhi.__doc__)
print(p.howmany.__doc__)

if __name__ == '__main__':
    pass
