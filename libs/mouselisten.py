#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from libs.thread_pool import global_thread_pool
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Event
from pynput import mouse

from libs.screenshot import GetGunInfo
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
        if pressed and self.enable_gun_info:
            if button == Button.left or button == Button.right:
                global_thread_pool.submit(self.execute_gun_info)

    def execute_gun_info(self):
        global_thread_pool.submit(self._execute_gun_info_task)

    def _execute_gun_info_task(self):
        gun_info_listener = GetGunInfo(self.parent)  # 获取装备信息, 传递父对象
        gun_info_listener.gun_info_signal.connect(self.parent.update_gun_info)

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听鼠标线程停止")
