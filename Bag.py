#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from Settings import *
from Item import *


class Bag:

    def __init__(self):
        self.items = []
        self.point = 0
        self.append(Item1(), 5)
        self.append(Item2(), 3)
        self.append(Item1(), 8)

    def append(self, item, count):
        print(item.__str__())
        for bag_block in self.items:
            if bag_block.item.id == item.id:
                bag_block.count += count
                return
        self.items.append(BagBlock(item, count))
        return

    def remove(self, item, count):
        for bag_block in self.items:
            if bag_block.item.id == item.id:
                if bag_block.count > count:
                    bag_block.count -= count
                else:
                    count = bag_block.count
                    self.items.remove(bag_block)
                return count
        return 0

    def draw(self):
        for i in range(len(self.items)):
            if self.point == i:
                print("→", end='')
            else:
                print(" ", end='')
            self.items[i].draw()



class BagBlock:

    def __init__(self, item, count):
        self.item = item
        self.count = count

    def append(self):
        pass

    def draw(self):
        print("% 5s % 3d %s" %(self.item.name, self.count, self.item.description))