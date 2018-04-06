#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = '方昕成'

list = []
x = 0
#name = input("please input data name:")
file = open("data.txt")
while 1:
  x = x + 1
  line = file.readline()
  if not line:
      break
  list.append(line) # do something
file.close()
list.append(name)
with open('data.txt', 'a', encoding='utf-8') as f:
    f.write(str(list[int(x-1)])+'\n')
    print('input success')
    f.close()
print(list[2][0:-1])