#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pynput
from pynput.keyboard import Key

class Listener:
    def __init__(self):
        self.press_list = []
        self.listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)

    def listen(self):
        self.listener.start()
        self.listener.join()

        self.listener.start()

    def on_press(self, key):
        if key not in self.press_list:
            self.press_list.append(key)
        else:
            return
        try:
            print('alphanumeric key     {0} pressed'.format(key.char))  # 应该记录下之前有没有ctrl、alt、和shift按下
        except AttributeError:
            print('special key {0} pressed'.format(key))

    def on_release(self, key):
        if key in self.press_list:
            self.press_list.remove(key)
        else:
            print("松开了未按下的按键，请检查是否按下ctrl，alt及shift")
        print('{0} released'.format(key))
        if key == Key.esc:
            return False