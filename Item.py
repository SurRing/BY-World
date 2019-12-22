#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Item:

    def __init__(self, name="无", id=0, description="暂无描述"):
        self.name = name
        self.id = id
        self.description = description

    def __str__(self):
        return "% 5s % 3d %s" %(self.name, self.id, self.description)


class Item1(Item):

    def __init__(self):
        super().__init__("item1", 1)


class Item2(Item):

    def __init__(self):
        super().__init__("item2", 2)


