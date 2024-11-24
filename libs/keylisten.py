#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time
from threading import Event, Thread

from PySide6.QtCore import QObject
from pynput import keyboard
from pynput.keyboard import Key

from libs.global_variable import GDV, THREAD_POOL
from libs.gun_info import GetGunInfo
from libs.screenshot import get_car, get_inventory, get_shooting_state, screen_capture_full
from tools.active_window import get_active_window_info
from tools.log import logger


class KeyListen(Thread, QObject):

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
        keys = str(keys.name if isinstance(keys, Key) else keys.char).lower()
        if get_active_window_info():
            # 定义替换字典
            replace_dict = {
                "!": "1",
                "@": "2",
                "#": "3",
                "$": "4",
                "%": "5"
            }
            keys = replace_dict.get(keys, keys)
            if keys == "tab":  # 监听到按键 'tab'
                if GDV.enable_key_recognition:  # 如果键盘识别背包开启
                    time.sleep(0.3)
                    self._get_gun_information()
                else:
                    GDV.enable_key_recognition = True
                    self._shooting_state()  # 获取射击状态

            elif keys == "esc":  # 监听到按键 'esc'
                GDV.enable_mouse_recognition = False
                GDV.enable_key_recognition = True
                self._shooting_state()

            elif keys in ["1","2"]:
                self.parent.state_win.update_state_gun_info(keys)  # 更新 state_win 枪械信息
                self._shooting_state()
                self.parent.update_home_current_gun()  # 更新当前枪械

            elif keys in ["3", "4","x", "5", "m"]:
                self._shooting_state()

            elif keys in ['z', 'c', 'ctrl_l', 'space']:
                self.parent.state_win.update_posture(keys)

            elif keys in ['f']:
                get_car()

    def _get_gun_information(self):
        # 获取枪械信息
        screen_capture_full()
        if get_inventory():
            if GDV.shooting_state == "fired":
                GDV.shooting_state = "stop"
                self.parent.state_win.update_state_shooting_state()
            GDV.enable_mouse_recognition = True  # 关闭鼠标识别
            GDV.enable_key_recognition = False
            GetGunInfo()  # 持续更新枪械信息
            self.parent.update_home_gun_info(GDV.weapon_information)
        else:
            GDV.enable_mouse_recognition = False

    def _shooting_state(self):  # 获取射击状态
        THREAD_POOL.submit(get_shooting_state).result()
        self.parent.state_win.update_state_shooting_state() # 更新射击状态

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听键盘线程停止")
