#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from Position import Position
import Creatures


class Player(Creatures.Creatures):

    def __init__(self):
        super().__init__()
        self.position = Position(0,0)
        self.img = "@"
        self.name = "小@"

