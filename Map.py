#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from Settings import *
from Position import Position
import Player

def rotate(matrix):#左旋
    matrix[:] = map(list, zip(*matrix))
    matrix[:] = matrix[::-1]

class MapDealer:

    def __init__(self):
        self.map = [[Block(x, y) for y in range(SIZE)] for x in range(SIZE)]
        self.player = Player.Player()
        self.map[0][0].contain = self.player

    def draw(self):
        map_img = [[0 if block.contain == None else block.contain.img for block in row] for row in self.map]
        rotate(map_img)
        for row in map_img:
            for block in row:
                print(block, end=' ')
            print()

    def move(self, origin, target):
        if not (0<=target.x<=SIZE-1 and 0<=target.y<=SIZE-1):
            print("越界")
            return False
        elif self.map[target.x][target.y].contain != None:
            print("目标位置存在物体")
            return False
        else:
            self.map[target.x][target.y].enter(self.map[origin.x][origin.y].leave())
            print("玩家向%s移动了" %target)
            return True

class Block:

    def __init__(self, x, y):
        self.position = Position(x,y)
        self.contain = None

    def leave(self):
        leave_thing = self.contain
        self.contain = None
        return leave_thing

    def enter(self, enter_thing):
        self.contain = enter_thing
        enter_thing.position = self.position
