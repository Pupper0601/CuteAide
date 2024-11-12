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
        active_window = get_active_window_info()
        # if "PUBG" in active_window["window_title"]:
        if True:
            if keys == "tab":  # 监听到按键 'tab'
                if global_variable.enable_key_recognition:
                    time.sleep(0.5) # 等待0.5秒, 等待背包打开
                    GetGunInfo()  # 更新枪械信息
                    self.parent.update_home_gun_info(global_variable.weapon_information)
                    global_variable.enable_mouse_recognition = False    # 关闭鼠标识别
                    global_variable.enable_key_recognition = False
                else:
                    GetGunInfo()  # 更新枪械信息
                    self.parent.update_home_gun_info(global_variable.weapon_information)
                    global_variable.enable_key_recognition = True
                    global_variable.enable_mouse_recognition = False
            elif keys == "esc":  # 监听到按键 'esc'
                global_variable.enable_mouse_recognition = False
                global_variable.enable_key_recognition = True
            elif keys in ["1", "!"]:
                if len(global_variable.weapon_information) > 0:
                    if global_variable.weapon_information["gun_1"]["weapon"][1] != "weapon_none":
                        self.parent.state_win.update_state_gun_info(keys)
                        self.parent.update_home_current_gun(keys)
                        global_variable.shooting_state = "fired"
                        self.parent.state_win.update_state_shooting_state()
                    elif global_variable.weapon_information["gun_2"]["weapon"][1] != "weapon_none":
                        self.parent.state_win.update_state_gun_info("2")
                        self.parent.update_home_current_gun("2")
                        global_variable.shooting_state = "fired"
                        self.parent.state_win.update_state_shooting_state()
                    global_variable.missile_stop_gun_5 = False
            elif keys in ["2", "@"]:
                if len(global_variable.weapon_information) > 0:
                    if global_variable.weapon_information["gun_2"]["weapon"][1] != "weapon_none":
                        self.parent.state_win.update_state_gun_info(keys)
                        self.parent.update_home_current_gun(keys)
                        global_variable.shooting_state = "fired"
                        self.parent.state_win.update_state_shooting_state()
                    elif global_variable.weapon_information["gun_1"]["weapon"][1] != "weapon_none":
                        self.parent.state_win.update_state_gun_info("1")
                        self.parent.update_home_current_gun("1")
                        global_variable.shooting_state = "fired"
                        self.parent.state_win.update_state_shooting_state()
                    global_variable.missile_stop_gun_5 = False
            elif keys in ["3","4","#","$",]:
                global_variable.shooting_state = "stop"
                self.parent.state_win.update_state_shooting_state()
            elif keys in ["x","X"]:
                if global_variable.missile_stop_gun_5:
                    global_variable.shooting_state = "stop"
                    self.parent.state_win.update_state_shooting_state()
                elif not global_variable.missile_stop_gun_x:
                    global_variable.shooting_state = "stop"
                    self.parent.state_win.update_state_shooting_state()
                    global_variable.missile_stop_gun_x = True
                elif global_variable.missile_stop_gun_x:
                    global_variable.shooting_state = "fired"
                    self.parent.state_win.update_state_shooting_state()
                    global_variable.missile_stop_gun_x = False
            elif keys in ["5", "%"]:
                global_variable.shooting_state = "stop"
                self.parent.state_win.update_state_shooting_state()
                global_variable.missile_stop_gun_5 = True
            elif keys in ['z',"Z", 'c',"C", 'ctrl_l', 'space']:
                self.parent.state_win.update_posture(keys)


    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听键盘线程停止")

