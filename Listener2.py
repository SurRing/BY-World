#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pynput
from pynput.keyboard import Key

move_list = ['w', 'a', 's', 'd']

class Listener:
    def __init__(self):
        self.press_list = []
        self.listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

    def listen(self):
        self.listener.start()
        self.listener.join()
        self.listener.stop()
        return self.key_process()

    def on_press(self, key):
        try:
            if key.char in move_list:
                self.press_list.append(key.char)
                return False
        except:
            self.press_list.append(key)

    def on_release(self, key):
        if key in self.press_list:
            self.press_list.remove(key)

    def key_process(self):
        return self.press_list[0]