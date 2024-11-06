#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from threading import Thread, Event
from PySide6.QtCore import QThread, Signal
from pynput import keyboard
from pynput.keyboard import Key
from libs.screenshot import GetGunInfo

from tools.log import logger


class KeyListen(QThread):
    key_pressed = Signal(str)  # 定义信号

    def __init__(self, parent=None):
        super(KeyListen, self).__init__(parent)
        self.listener = None
        self.stop_event = Event()
        self.task_thread = None
        self.parent = parent  # 保存父对象
        self.first_tab_pressed = False  # 标记是否第一次按下 tab 键

    def run(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        logger.info("监听键盘线程启动")
        self.listener.join()

    def on_press(self, key):
        try:
            if key == Key.tab:  # 监听到按键 'tab'
                self.key_pressed.emit('tab')
                if not self.first_tab_pressed:
                    self.first_tab_pressed = True
                    self.parent.mouse_listener.enable_gun_info = True
                    self.execute_gun_info()
                else:
                    self.execute_gun_info()
                    self.first_tab_pressed = False
                    self.parent.mouse_listener.enable_gun_info = False
                    self.stop_event.set()
            elif key == Key.esc:  # 监听到按键 'esc'
                self.key_pressed.emit('esc')
                self.execute_gun_info()
                self.parent.mouse_listener.enable_gun_info = False
                self.stop_event.set()
        except AttributeError:
            pass

    def execute_gun_info(self):
        gun_info_listener = GetGunInfo(self.parent)  # 获取装备信息, 传递父对象
        gun_info_listener.gun_info_signal.connect(self.parent.update_gun_info)

    def handle_delayed_task(self, key):
        # 处理延迟任务
        def task():
            while not self.stop_event.is_set():
                gun_info_listener = GetGunInfo(self.parent)    # 获取装备信息, 传递父对象
                gun_info_listener.gun_info_signal.connect(self.parent.update_gun_info)  # 连接信号
            self.stop_event.clear()

        self.task_thread = Thread(target=task)
        self.task_thread.start()

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听键盘线程停止")
