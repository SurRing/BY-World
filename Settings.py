#!/usr/bin/env python
# _*_ coding:utf-8 _*

from Position import Position

SIZE = 20
move_dict = {"w":Position(0,1), "a":Position(-1,0), "s":Position(0,-1), "d":Position(1,0)}
describe_dict = {"w":"北", "a":"西", "s":"南", "d":"东"}
system_operation = ["bag",]
bag_actions = ["w","s"]
