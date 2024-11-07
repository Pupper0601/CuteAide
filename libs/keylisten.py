#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from threading import Event

from libs.thread_pool import global_thread_pool
from PySide6.QtCore import QThread, Signal
from pynput import keyboard
from pynput.keyboard import Key
from libs.screenshot import GetGunInfo, get_inventory

from tools.log import logger


class KeyListen(QThread):
    key_pressed = Signal(str)  # 定义信号

    def __init__(self, parent=None):
        super(KeyListen, self).__init__(parent)
        self.listener = None
        self.stop_event = Event()
        self.parent = parent  # 保存父对象


    def run(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        logger.info("监听键盘线程启动")
        self.listener.join()

    def on_press(self, key):
        # 监听按键
        try:
            if key == Key.tab:  # 监听到按键 'tab'
                self.key_pressed.emit('tab')  # 发送信号
                global_thread_pool.submit(self.check_inventory_and_execute)
            elif key == Key.esc:  # 监听到按键 'esc'
                self.key_pressed.emit('esc')
                self.parent.mouse_listener.enable_gun_info = False
                self.stop_event.set()
            elif key.char in ['1', '2']:
                self.parent.update_state_win(key.char)

        except AttributeError:
            pass

    def check_inventory_and_execute(self):
        # 检查当前是否为背包状态
        if get_inventory():  # 如果当前为背包状态
            self.execute_gun_info()
            self.parent.mouse_listener.enable_gun_info = True  # 控制鼠标点击识别
        else:
            logger.info("当前不是背包状态")
            self.parent.mouse_listener.enable_gun_info = False
            self.stop_event.set()

    def execute_gun_info(self):
        global_thread_pool.submit(self._execute_gun_info_task)   # 提交任务

    def _execute_gun_info_task(self):
        gun_info_listener = GetGunInfo(self.parent)  # 获取装备信息, 传递父对象
        gun_info_listener.gun_info_signal.connect(self.parent.update_gun_info)  # 连接信号

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听键盘线程停止")
