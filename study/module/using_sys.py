#coding=utf-8
#Filename: using-sys.py

import sys

print('the commond line arguement are')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')
