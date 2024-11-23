#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time
from threading import Event, Thread

from PySide6.QtCore import QObject
from pynput import mouse
from pynput.mouse import Button

from libs.global_variable import GDV
from libs.gun_info import GetGunInfo
from libs.screenshot import screen_capture_full
from tools.active_window import get_active_window_info
from tools.log import logger


class MouseListen(Thread, QObject):
    def __init__(self, parent=None):
        Thread.__init__(self)
        QObject.__init__(self)
        self.listener = None
        self.stop_event = Event()
        self.parent = parent  # 保存父对象

    def run(self):  # 监听鼠标
        self.listener = mouse.Listener(on_click=self.on_click)  # 监听鼠标点击
        self.listener.start()
        logger.info("监听鼠标线程启动")

    def on_click(self, x, y, button, pressed):
        if get_active_window_info():
            # if True:
            if not pressed and GDV.enable_mouse_recognition:
                if button == Button.right:
                    time.sleep(0.3)
                    screen_capture_full()
                    GetGunInfo()
                    self.parent.update_home_gun_info(GDV.weapon_information)

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听鼠标线程停止")
