#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os

from Position import Position
from Settings import *
import Listener2
import Map


class MainHandler:

    def __init__(self):
        self.msg_log = []#创建信息记录
        self.mapDealer = Map.MapDealer(self)#创建地图控制器
        self.player = self.mapDealer.player#链接主人物
        self.state_action = self.map_state#表明当前所处状态，初始化为地图状态
        self.msg_log.append("主控器就绪")

    def turn(self):
        # 清屏
        i = os.system("cls")

        # 状态行为
        self.state_action()

        # 用户行为
        self.user_act()

    def map_state(self):
        print("map_state")
        # 执行生物行为
        self.mapDealer.run()

        # 显示地图
        self.mapDealer.draw()

        # 打印信息
        self.print_msg()

    def bag_state(self):
        print("bag_state")
        self.player.bag.draw()

    def append_msg(self, msg):
        self.msg_log.append(msg)

    def print_msg(self):
        for msg in self.msg_log[-5:]:
            print(msg)

    def user_act(self):
        # 接收用户操作
        act = Listener2.Listener().listen()

        # 执行用户行为
        if act in system_operation:# 系统操作
            if self.state_action != self.bag_state:
                self.state_action = self.bag_state
            else:
                self.state_action = self.map_state

        if self.state_action == self.map_state:# 地图状态操作
            if act in move_dict.keys():  # 移动
                self.move(act)
        elif self.state_action == self.bag_state:
            if act in bag_actions:
                if act == "w" and self.player.bag.point !=0:
                    self.player.bag.point -=1
                if act == "s" and self.player.bag.point != len(self.player.bag.items)-1:
                    self.player.bag.point += 1

    def move(self, act):
        if act in move_dict.keys():
            self.mapDealer.move(self.player.position, self.player.position + move_dict[act])
        self.append_msg(self.mapDealer.player.name + "现在处于" + self.mapDealer.player.position)
        self.mapDealer.count += self.mapDealer.player.action_time













if __name__ == "__main__":
    mainHandler = MainHandler()
    while 1:
        mainHandler.turn()
