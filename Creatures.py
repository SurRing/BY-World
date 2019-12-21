#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import random
from Position import Position
import Map


class Creature:

    def __init__(self, position, mapDealer):
        self.flag = 0
        self.mapDealer = mapDealer
        self.position = position
        self.img = "1"
        self.name = "某生物"

    def born(self):
        if self.mapDealer.map[self.position.x][self.position.y].contain:print("替换原物体："+self.mapDealer.map[self.position.x][self.position.y].contain)
        self.mapDealer.map[self.position.x][self.position.y].contain = self

    def run(self, count):
        return "pass"


class PeaceCreature(Creature):

    def __init__(self, position, mapDealer):
        super().__init__(position, mapDealer)

    def run(self, count):
        if self.flag >= count:return
        act = random.choice(['w', 'a', 's', 'd'])
        self.mapDealer.move(self.position, self.position+Map.move_dict[act])
        self.flag+=1