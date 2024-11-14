#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import psutil
import win32gui
import win32process

from libs import global_variable


def get_active_window_info():
    hwnd = win32gui.GetForegroundWindow()  # 获取当前活动窗口句柄
    _, pid = win32process.GetWindowThreadProcessId(hwnd)  # 获取窗口对应的进程ID
    process = psutil.Process(pid)  # 获取进程信息
    window_title = win32gui.GetWindowText(hwnd)  # 获取窗口标题
    process_name = process.name()  # 获取进程名称
    _active_window =  {
        "window_title": window_title,
        "process_name": process_name,
        "pid"         : pid
    }
    if "PUBG" in _active_window["window_title"]:
        return True
    else:
        return False