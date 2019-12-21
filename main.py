#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from Position import Position
import Listener2
import Map

move_dict = {"w":Position(0,1), "a":Position(-1,0), "s":Position(0,-1), "d":Position(1,0)}
describe_dict = {"w":"北", "a":"西", "s":"南", "d":"东"}
mapDealer = Map.MapDealer()

def move(act, mapDealer):
    if act in move_dict.keys():
        mapDealer.move(mapDealer.player.position, mapDealer.player.position+move_dict[act])
    print("玩家现在处于"+mapDealer.player.position)

print("开始了")
while 1:
    mapDealer.draw()
    act = Listener2.Listener().listen()
    move(act, mapDealer)


