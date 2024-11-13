#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from libs.cache import ImageCache
from concurrent.futures import ThreadPoolExecutor

# 创建一个全局的线程池
THREAD_POOL = ThreadPoolExecutor()

CACHE = ImageCache().source_data

enable_mouse_recognition = False
enable_key_recognition = True
weapon_information = {} # 武器信息
posture_state_button = "c"  # 默认切换姿势键

in_car = "no"  # 是否在车上, no为不在车上, yes为在车上
posture_state = "stand" # 默认站立
shooting_state = "fired"    # 默认射击状态
opening_method = "click"  # 默认开镜方式, 长按为 "long_press"
continuous_clicks = "close"  # 默认连点, close为关闭, open为开启

current_weapon_information = {} # 当前武器信息
fire_weapon = "1"   # 默认开火武器
missile_stop_gun_x = False  # x收枪
missile_stop_gun_5 = False  # 投掷物收枪

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