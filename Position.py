#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Position(-self.x, -self.y)

    def __pos__(self):
        return Position(self.x, self.y)

    def __add__(self, other):
        try:
            return Position(self.x+other.x, self.y+other.y)
        except:
            return other+self.__str__()

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return "(%d,%d)" %(self.x, self.y)
