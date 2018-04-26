#!/usr/bin/env python
# coding=utf-8

"""
@version: ??
@author: chengyoufu
@license: Apache Licence 
@contact: chengyoufu@gmail.com
@site: http://www.xxxxx.com
@software: PyCharm
@file: inherit.py
@time: 2015/10/3 22:57
"""

class schoolmember():
    '''Represents any school member'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Initialized schoolmember')

    def tell(self):
        '''Tell my details.'''
        print('Name:%s Age:%s'%(self.name,self.age))


class teacher(schoolmember):
    ''' Represents a teacher'''
    def __init__(self,name,age,salary):
        schoolmember.__init__(self,name,age)
        self.salary=salary
        print('Initialized a teacher')

    def tell(self):
        schoolmember.tell(self)
        print('salary:%d'%self.salary)

class student(schoolmember):
    '''Represents a student'''
    def __init__(self,name,age,marks):
        schoolmember.__init__(self,name,age)
        self.marks = marks
        print('Initialized a student')
        
    def tell(self):
        schoolmember.tell(self)
        print('Marks:%s'%self.marks)

class nuonuo():
    def __init__(self):
        pass

    def tell(self):
        print('this is nuonuo ')
t=teacher('leo cheng',30,10000)
s=student('nuonuo',10,'A')
n=nuonuo()


members = [t,s,n]

for member in members:
    member.tell()

