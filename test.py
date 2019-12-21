#!/usr/bin/env python
# _*_ coding:utf-8 _*_
a = [[1,2],[3,4]]
for row in a:
    print(row)
def rotate(matrix):#左旋
    matrix[:] = map(list, zip(*matrix))
    matrix[:] = matrix[::-1]
rotate(a)
for row in a:
    print(row)