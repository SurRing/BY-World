#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from Position import Position
import Creatures


class Player(Creatures.Creature):

    def __init__(self, position, mapDealer):
        super().__init__(position, mapDealer)
        self.img = "@"
        self.name = "小@"

