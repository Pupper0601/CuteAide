#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time
from threading import Event, Thread

from PySide6.QtCore import QObject, Signal
from pynput import keyboard
from pynput.keyboard import Key

from libs import global_variable
from libs.gun_info import GetGunInfo
from libs.screenshot import get_car
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
        keys = str(keys.name if isinstance(keys, Key) else keys.char)
        if get_active_window_info():
        # if True:
            if keys == "tab":  # 监听到按键 'tab'
                if global_variable.enable_key_recognition:
                    time.sleep(0.3) # 等待0.5秒, 等待背包打开
                    GetGunInfo()  # 更新枪械信息
                    self.parent.update_home_gun_info(global_variable.weapon_information)
                    global_variable.enable_mouse_recognition = False    # 关闭鼠标识别
                    global_variable.enable_key_recognition = False    # 关闭键盘识别
                else:
                    GetGunInfo()  # 更新枪械信息
                    self.parent.update_home_gun_info(global_variable.weapon_information)
                    global_variable.enable_key_recognition = True
                    global_variable.enable_mouse_recognition = False
            elif keys == "esc":  # 监听到按键 'esc'
                global_variable.enable_mouse_recognition = False
                global_variable.enable_key_recognition = True
                global_variable.shooting_state = "stop"
                self.parent.state_win.update_state_shooting_state()
            elif keys in ["1", "!"]:
                self._update_weapon_state("gun_1", "gun_2", keys)
            elif keys in ["2", "@"]:
                self._update_weapon_state("gun_2", "gun_1", keys)
            elif keys in ["3","4","#","$","x", "X", "5", "%"]:
                global_variable.shooting_state = "stop"
                self.parent.state_win.update_state_shooting_state()
            elif keys in ['z',"Z", 'c',"C", 'ctrl_l', 'space']:
                self.parent.state_win.update_posture(keys)
            elif keys in ['F', 'f']:
                get_car()

    def _update_weapon_state(self, primary_gun, secondary_gun, keys):
        if len(global_variable.weapon_information) > 0:
            if global_variable.weapon_information[primary_gun]["weapon"][1] != "weapon_none":
                self.parent.state_win.update_state_gun_info(keys)
                self.parent.update_home_current_gun(keys)
                global_variable.shooting_state = "fired"
                self.parent.state_win.update_state_shooting_state()
            elif global_variable.weapon_information[secondary_gun]["weapon"][1] != "weapon_none":
                self.parent.state_win.update_state_gun_info("2" if primary_gun == "gun_1" else "1")
                self.parent.update_home_current_gun("2" if primary_gun == "gun_1" else "1")
                global_variable.shooting_state = "fired"
                self.parent.state_win.update_state_shooting_state()


    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听键盘线程停止")

