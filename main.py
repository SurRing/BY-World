#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from Position import Position
import Listener2
import Map

move_dict = {"w":Position(0,1), "a":Position(-1,0), "s":Position(0,-1), "d":Position(1,0)}
describe_dict = {"w":"北", "a":"西", "s":"南", "d":"东"}

msg_log = []
mapDealer = Map.MapDealer(msg_log)

def move(act, mapDealer):
    if act in move_dict.keys():
        mapDealer.move(mapDealer.player.position, mapDealer.player.position+move_dict[act])
    msg_log.append(mapDealer.player.name+"现在处于"+mapDealer.player.position)


def main():
    msg_log.append("开始了")

    while 1:
        # 清屏
        i = os.system("cls")

        # 执行生物行为
        mapDealer.run()

        # 显示地图
        mapDealer.draw()

        # 打印信息
        for msg in msg_log[-5:]:
            print(msg)

        # 监听用户操作
        act = Listener2.Listener().listen()

        # 执行用户行为
        move(act, mapDealer)



if __name__ == "__main__":
    main()
