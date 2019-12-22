#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from Settings import *
from Position import Position
import Player
import Creatures

move_dict = {"w":Position(0,1), "a":Position(-1,0), "s":Position(0,-1), "d":Position(1,0)}


def rotate(matrix):#左旋
    matrix[:] = map(list, zip(*matrix))
    matrix[:] = matrix[::-1]


class MapDealer:

    def __init__(self, mainHandler):
        self.mainHandler = mainHandler
        self.map = [[Block(x, y) for y in range(SIZE)] for x in range(SIZE)]
        self.count = 0
        self.creatures = []

        self.player = Player.Player(Position(0,0), self)
        self.player.born()

        creature = Creatures.PeaceCreature(Position(SIZE-1,SIZE-1), self)
        creature.born()
        self.creatures.append(creature)

    def run(self):
        for creature in self.creatures:
            creature.run(self.count)

    def draw(self):
        map_img = [[0 if not block.contain else block.contain.img for block in row] for row in self.map]
        rotate(map_img)
        for row in map_img:
            for block in row:
                print(block, end=' ')
            print()

    def move(self, origin, target):
        if not (0<=target.x<=SIZE-1 and 0<=target.y<=SIZE-1):
            self.mainHandler.append_msg("越界")
            return False
        elif self.map[target.x][target.y].contain:
            self.mainHandler.append_msg("目标位置存在物体")
            return False
        else:
            self.map[target.x][target.y].enter(self.map[origin.x][origin.y].leave())
            self.mainHandler.append_msg("%s向%s移动了" %(self.map[target.x][target.y].contain.name, target))
            return True


class Block:

    def __init__(self, x, y):
        self.position = Position(x, y)
        self.contain = None

    def leave(self):
        leave_thing = self.contain
        self.contain = None
        return leave_thing

    def enter(self, enter_thing):
        self.contain = enter_thing
        enter_thing.position = self.position
