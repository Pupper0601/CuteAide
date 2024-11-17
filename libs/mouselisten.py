#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time

from threading import Thread, Event
from pynput import mouse

from libs.global_variable import global_variable

from libs.gun_info import GetGunInfo
from libs.pressure import Pressure
from tools.active_window import get_active_window_info
from tools.log import logger
from pynput.mouse import Button


class MouseListen(Thread):
    def __init__(self, parent=None):
        super(MouseListen, self).__init__()
        self.listener = None
        self.stop_event = Event()
        self.parent = parent  # 保存父对象

    def run(self):  # 监听鼠标
        self.listener = mouse.Listener(on_click=self.on_click)  # 监听鼠标点击
        self.listener.start()
        logger.info("监听鼠标线程启动")

    def on_click(self, x,y, button, pressed):
        if get_active_window_info():
        # if True:
            if not pressed and global_variable.enable_mouse_recognition:
                self.parent.update_way("识别中......")
                if button == Button.right:
                    GetGunInfo()
                    self.parent.update_home_gun_info(global_variable.weapon_information)
                    self.parent.update_way("识别完成")

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听鼠标线程停止")
