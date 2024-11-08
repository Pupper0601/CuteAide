#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from threading import Event, Thread

from libs.thread_pool import global_thread_pool
from PySide6.QtCore import QObject, QThread, Signal
from pynput import keyboard
from pynput.keyboard import Key
from libs.screenshot import GetGunInfo, get_inventory

from tools.log import logger


class KeyListen(Thread, QObject):
    key_pressed = Signal(str)  # 定义信号

    def __init__(self, parent=None):
        Thread.__init__(self)
        QObject.__init__(self)
        self.listener = None
        self.stop_event = Event()
        self.parent = parent  # 保存父对象


    def run(self):
        self.listener = keyboard.Listener(on_press=self.on_pressed)
        self.listener.start()
        logger.info("监听键盘线程启动")

    def on_pressed(self, keys):
        # 监听按键
        keys = str(keys.name if isinstance(keys, Key) else keys.char)
        logger.debug(f"按键 {keys} 被按下")  # 添加日志记录
        try:
            if keys == "tab":  # 监听到按键 'tab'
                self.key_pressed.emit('tab')  # 发送信号
                global_thread_pool.submit(self.check_inventory_and_execute)
            elif keys == "esc":  # 监听到按键 'esc'
                self.key_pressed.emit('esc')
                self.parent.mouse_listener.enable_gun_info = False
                self.stop_event.set()
            elif keys in ['1', '2']:
                self.parent.update_state_win(keys)
                self.parent.update_current_gun(keys)
            elif keys in ['z', 'c']:
                self.parent.posture_key(keys)
            elif keys == "space":  # 监听到按键 '空格'
                self.parent.posture_key('space')
            elif keys == "ctrl_l":  # 监听到按键 'ctrl'
                self.parent.posture_key('ctrl')

        except AttributeError:
            pass

    def check_inventory_and_execute(self):
        # 检查当前是否为背包状态
        if get_inventory():  # 如果当前为背包状态
            self.parent.update_way("识别中......")
            self.execute_gun_info()
            self.parent.mouse_listener.enable_gun_info = True  # 控制鼠标点击识别
        else:
            logger.info("当前不是背包状态")
            self.parent.update_way("等待打开背包识别")
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
