#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time

from threading import Thread, Event
from pynput import mouse
from libs.global_variable import THREAD_POOL

from libs.gun_info import GunInfo
from tools.active_window import get_active_window_info
from tools.log import logger
from pynput.mouse import Button


class MouseListen(Thread):
    def __init__(self, parent=None):
        super(MouseListen, self).__init__()
        self.listener = None
        self.stop_event = Event()
        self.parent = parent  # 保存父对象
        self.enable_gun_info = False  # 标记是否执行 GetGunInfo 方法

    def run(self):  # 监听鼠标
        self.listener = mouse.Listener(on_click=self.on_click)  # 监听鼠标点击
        self.listener.start()
        logger.info("监听鼠标线程启动")

    def on_click(self, x,y, button, pressed):
        active_window = get_active_window_info()
        if "PUBG" in active_window["window_title"]:
            if pressed and self.enable_gun_info:
                self.parent.update_way("识别中......")
                if button == Button.left or button == Button.right:
                    THREAD_POOL.submit(self.update_gun_info)
                    self.parent.update_way("识别完成")
        else:
            self.enable_gun_info = False
            self.parent.update_way("当前不在游戏中")

    def update_gun_info(self):
        self.parent.update_gun_info(GunInfo().gun_info)

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听鼠标线程停止")
