#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import threading

from concurrent.futures import ThreadPoolExecutor

# 创建一个全局的线程池
THREAD_POOL = ThreadPoolExecutor()

CACHE = None

global_screenshot = None

# enable_mouse_recognition = False
# enable_key_recognition = True
# weapon_information = {} # 武器信息
# posture_state_button = "c"  # 默认切换姿势键
#
# in_car = "no"  # 是否在车上, no为不在车上, yes为在车上
# posture_state = "stand" # 默认站立
# shooting_state = "fired"    # 默认射击状态
# opening_method = "click"  # 默认开镜方式, 长按为 "long_press"
#
# current_weapon_information = {} # 当前武器信息
# fire_weapon = "1"   # 默认开火武器

class Observable:
    def __init__(self):
        self._observers = []
        self._last_notify_time = 0
        self._notify_lock = threading.Lock()
        self._timer = None
        self._auto_update_enabled = True  # 添加标志位

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        if not self._auto_update_enabled:
            return
        with self._notify_lock:
            if self._timer:
                self._timer.cancel()
            self._timer = threading.Timer(0.5, self._execute_notify)
            self._timer.start()

    def _execute_notify(self):
        with self._notify_lock:
            for observer in self._observers:
                observer.update()
            from libs.pressure import Pressure
            Pressure()

class GlobalVariable(Observable):
    def __init__(self):
        super().__init__()
        self._enable_mouse_recognition = False
        self._enable_key_recognition = True
        self._weapon_information = {}
        self._posture_state_button = "c"
        self._in_car = "no"
        self._posture_state = "stand"
        self._shooting_state = "fired"
        self._opening_method = "click"
        self._continuous_clicks = "close"
        self._current_weapon_information = {}
        self._fire_weapon = "1"
        self._global_screenshot = None

    @property
    def enable_mouse_recognition(self):
        return self._enable_mouse_recognition

    @enable_mouse_recognition.setter
    def enable_mouse_recognition(self, value):
        self._enable_mouse_recognition = value
        self.notify_observers()

    @property
    def enable_key_recognition(self):
        return self._enable_key_recognition

    @enable_key_recognition.setter
    def enable_key_recognition(self, value):
        self._enable_key_recognition = value
        self.notify_observers()

    @property
    def weapon_information(self):
        return self._weapon_information

    @weapon_information.setter
    def weapon_information(self, value):
        self._weapon_information = value
        self.notify_observers()

    @property
    def posture_state_button(self):
        return self._posture_state_button

    @posture_state_button.setter
    def posture_state_button(self, value):
        self._enable_key_recognition = value

    @property
    def in_car(self):
        return self._in_car

    @in_car.setter
    def in_car(self, value):
        self._in_car = value
        self.notify_observers()

    @property
    def posture_state(self):
        return self._posture_state

    @posture_state.setter
    def posture_state(self, value):
        self._posture_state = value
        self.notify_observers()

    @property
    def shooting_state(self):
        return self._shooting_state

    @shooting_state.setter
    def shooting_state(self, value):
        self._shooting_state = value
        self.notify_observers()

    @property
    def opening_method(self):
        return self._opening_method

    @opening_method.setter
    def opening_method(self, value):
        self._opening_method = value
        self.notify_observers()

    @property
    def current_weapon_information(self):
        return self._current_weapon_information

    @current_weapon_information.setter
    def current_weapon_information(self, value):
        self._current_weapon_information = value
        self.notify_observers()

    @property
    def fire_weapon(self):
        return self._fire_weapon

    @fire_weapon.setter
    def fire_weapon(self, value):
        self._fire_weapon = value

    @property
    def global_screenshot(self):
        return self._global_screenshot

    @global_screenshot.setter
    def global_screenshot(self, value):
        self._global_screenshot = value

global_variable = GlobalVariable()



TRANSLATE = {
  "weapon_none": "无武器",
  "stock_none": "无枪托",
  "scope_none": "无倍镜",
  "muzzle_none": "无枪口",
  "grip_none": "无握把",
  "qingxin": "轻型握把",
  "zhijiao": "直角前握把",
  "banjie": "半截握把",
  "chuizhi": "垂直握把",
  "jiguang": "激光瞄准器",
  "muzhi": "拇指握把",
  "buchang-b": "后座补偿器",
  "buchang-c": "枪口补偿器",
  "buchang-j": "后座补偿器",
  "eliuquan.png": "扼流圈",
  "xiaoyan-b": "消焰器",
  "xiaoyan-c": "消焰器",
  "xiaoyan-j": "消焰器",
  "xiaoyin-b": "消音器",
  "xiaoyin-c": "消音器",
  "xiaoyin-j": "消音器",
  "yazui": "鸭嘴枪口",
  "zhituiqi": "枪口制退器",
  "hongdian": "红点瞄准镜",
  "quanxi": "全息瞄准镜",
  "x2": "2倍镜",
  "x3": "3倍镜",
  "x4": "4倍镜",
  "x6": "6倍镜",
  "x8": "8倍镜",
  "tosaiban": "托腮板",
  "zhanshu": "战术枪托",
  "zhedie": "折叠式枪托",
  "zhongxing": "重型枪托",
  "zidandai": "子弹袋",
  "AKM": "AKM",
  "M762": "Beryl M762",
  "G36C": "G36C",
  "M416": "M416",
  "M16A4": "M16A4",
  "SCARL": "SCAR-L",
  "MK47": "MK47 Mutant",
  "QBZ": "QBZ",
  "AUG": "AUG",
  "GROZA": "Groza",
  "ACE32": "ACE32",
  "K2": "K2",
  "FAMAS": "FAMAS",
  "98K": "Kar98K",
  "M24": "M24",
  "AWM": "AWM",
  "AMR": "Lynx AMR",
  "WIN94": "Win94",
  "MXNG": "莫辛纳甘步枪",
  "ZDZT": "自动装填步枪",
  "MINI14": "Mini14",
  "SKS": "SKS",
  "VSS": "VSS",
  "QBU": "QBU",
  "MK14": "Mk14",
  "MK12": "Mk12",
  "DLGNF": "德拉贡诺夫",
  "S686": "S686",
  "S12K": "S12K",
  "S1897": "S1897",
  "DBS": "DBS",
  "O12": "O12",
  "PP19": "PP-19 Bizon",
  "TMX": "汤姆逊冲锋枪",
  "UMP": "UMP",
  "UZI": "微型 UZI",
  "VECTOR": "Vector",
  "MP5K": "MP5K",
  "P90": "P90",
  "JS9": "JS9",
  "MP9": "MP9",
  "DP28": "DP-28",
  "M249": "M249",
  "MG3": "MG3"
}
