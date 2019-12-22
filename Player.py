#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from Position import Position
import Creatures
import Bag


class Player(Creatures.Creature):

    def __init__(self, position, mapDealer):
        super().__init__(position, mapDealer)
        self.action_time = 2
        self.img = "\033[36m@\033[0m"
        self.name = "小@"
        self.bag = Bag.Bag()

