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
from libs.screenshot import get_car, get_gun_position, get_inventory, get_shooting_state
from tools.active_window import get_active_window_info
from tools.log import logger


class KeyListen(Thread, QObject):

    def __init__(self, parent=None):
        Thread.__init__(self)
        QObject.__init__(self)
        self.listener = None
        self.stop_event = Event()
        self.parent = parent  # 保存父对象
        self.key_states = {}  # 添加字典来记录每个键的状态
        self._button_status = True

    def run(self):
        self.listener = keyboard.Listener(on_press=self.on_pressed,on_release=self.on_released)
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
            if keys not in self.key_states or not self.key_states[keys]:  # 检查键的状态
                self.key_states[keys] = True  # 设置键的状态为按下
                if keys == "tab":  # 监听到按键 'tab'
                    if GDV.enable_key_recognition:  # 如果键盘识别背包开启
                        self._get_gun_information()
                    else:
                        GDV.enable_key_recognition = True
                        self._shooting_state()

                elif keys == "esc":  # 监听到按键 'esc'
                    GDV.enable_mouse_recognition = False
                    GDV.enable_key_recognition = True
                    self._shooting_state()

                elif keys in ["1","2"]:
                    _gun = GDV.current_weapon_information
                    if len(_gun) > 0 and _gun["weapon"][1] != "weapon_none":
                        if GDV.shooting_state == "stop":
                            GDV.shooting_state = "fired"
                    else:
                        if GDV.shooting_state == "fired":
                            GDV.shooting_state = "stop"
                    self.parent.state_win.update_state_gun_info(keys)  # 更新 state_win 枪械信息
                    self.parent.state_win.update_state_shooting()
                    self.parent.update_home_current_gun()  # 更新当前枪械

                elif keys in ["x", "m"]:
                    if self._button_status:
                        if GDV.shooting_state == "fired":
                            GDV.shooting_state = "stop"
                            self.parent.state_win.update_state_shooting()
                            self._button_status = False
                    else:
                        self._shooting_state()
                        self._button_status = True

                elif keys in ["3", "4", "5"]:
                    self._shooting_state()

                elif keys in ['z', 'c', 'ctrl_l', 'space']:
                    self.parent.state_win.update_posture(keys)

                elif keys in ['f']:
                    get_car()

    def on_released(self, keys):
        keys = str(keys.name if isinstance(keys, Key) else keys.char).lower()
        self.key_states[keys] = False  # 重置键的状态

    def _get_gun_information(self):
        # 获取枪械信息
        start_time = time.time()
        _time = 0
        count = 0
        while _time <= 1:
            count += 1
            logger.info(f"第 {count} 次获取枪械信息")
            if get_inventory() and (get_gun_position("1") or get_gun_position("2")):
                if GDV.shooting_state == "fired":
                    GDV.shooting_state = "stop"
                    self.parent.state_win.update_state_shooting()
                GDV.enable_mouse_recognition = True  # 关闭鼠标识别
                GDV.enable_key_recognition = False
                GetGunInfo()  # 持续更新枪械信息
                self.parent.update_home_gun_info(GDV.weapon_information)
                break
            _time = time.time() - start_time
        else:
            GDV.enable_mouse_recognition = False

    def _shooting_state(self):  # 获取射击状态
        if GDV.shooting_state == "fired":
            GDV.shooting_state = "stop"
            self.parent.state_win.update_state_shooting()
            return
        else:
            _gun = GDV.current_weapon_information
            if len(_gun) > 0 and _gun["weapon"][1] != "weapon_none":
                start_time = time.time()
                _time = 0
                count = 0
                while _time <= 1:
                    count += 1
                    logger.info(f"第 {count} 次获取射击状态")
                    if get_shooting_state():
                        self.parent.state_win.update_state_shooting()
                        self._button_status = True
                        break
                    _time = time.time() - start_time
                else:
                    GDV.shooting_state = "stop"
                    logger.info(f"当前射击状态 --->>> 停止, {GDV.shooting_state}")
                    self.parent.state_win.update_state_shooting() # 更新射击状态

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
            logger.info("监听键盘线程停止")
