#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from ctypes import CDLL, c_char_p
from tools.paths import path_conn


class GhubDevice:
    info = None

    def __init__(self):
        try:
            self.gm = CDLL(path_conn("/ghub_device.dll"))  # ghubdlldir
            self.gm_ok = self.gm.device_open()
            self.gm.key_down.argtypes = [c_char_p]
            self.gm.key_up.argtypes = [c_char_p]
            if not self.gm_ok:
                self.info = '未安装ghub或者lgs驱动!!!'
            else:
                self.info = '驱动初始化成功!'
        except FileNotFoundError:
            self.info = '重要键鼠文件缺失'
            self.gm_ok = 0

    def _mouse_event(self, fun, *args):
        # 键鼠事件
        if self.gm_ok:  # 键鼠初始化成功
            try:
                if hasattr(self.gm, fun):   # 判断是否有该方法
                    return getattr(self.gm, fun)(*args) # 调用方法
                else:
                    return None
            except (NameError, OSError):
                self.info = '键鼠调用严重错误!!!'



    def mouse_R(self, x, y):    # 鼠标右键
        return self._mouse_event('moveR', int(x), int(y))

    def mouse_To(self, x, y):   # 鼠标移动
        return self._mouse_event('moveTo', int(x), int(y))

    def mouse_down(self, key=1):    # 鼠标按下
        return self._mouse_event('mouse_down', int(key))

    def mouse_up(self, key=1):  # 鼠标抬起
        return self._mouse_event('mouse_up', int(key))

    def scroll(self, num=1):    # 鼠标滚轮
        return self._mouse_event('scroll', int(num))

    def key_down(self, key):    # 键盘按下
        return self._mouse_event('key_down', key.encode('utf-8'))

    def key_up(self, key):  # 键盘抬起
        return self._mouse_event('key_up', key.encode('utf-8'))

    def device_close(self): # 关闭驱动
        return self._mouse_event('device_close')


if __name__ == '__main__':
    g = GhubDevice()
    print(g.info)
    print(g.gm_ok)
    print(g.mouse_R(100, 100))
    print(g.mouse_To(100, 100))
    print(g.mouse_down(1))
    print(g.mouse_up(1))
    print(g.scroll(1))
    print(g.key_down('a'))
    print(g.key_up('a'))
    print(g.device_close())