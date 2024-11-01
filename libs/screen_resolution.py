#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import win32api
import win32con

def get_monitor_info():
    monitors = []
    monitor_enum_proc = lambda hMonitor, hdcMonitor, lprcMonitor, dwData: monitors.append(lprcMonitor)
    win32api.EnumDisplayMonitors(None, None, monitor_enum_proc, 0)
    return monitors

monitors = get_monitor_info()
for i, monitor in enumerate(monitors):
    width = monitor[2] - monitor[0]
    height = monitor[3] - monitor[1]
    print(f"第{i+1}个显示器分辨率为：{width} x {height}")

