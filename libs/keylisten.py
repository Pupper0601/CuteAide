#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time
from threading import Event, Thread

from PySide6.QtCore import QObject, Signal
from pynput import keyboard
from pynput.keyboard import Key

from libs.gun_info import GunInfo
from tools.active_window import get_active_window_info

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
        active_window = get_active_window_info()
        if "PUBG" in active_window["window_title"]:
            if keys == "tab":  # 监听到按键 'tab'
                self.key_pressed.emit('tab')  # 发送信号
                self.parent.update_gun_info(GunInfo().gun_info)
                self.parent.mouse_listener.enable_gun_info = True
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
        else:
            self.parent.mouse_listener.enable_gun_info = False
            self.parent.update_way("当前不在游戏中")


    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听键盘线程停止")

