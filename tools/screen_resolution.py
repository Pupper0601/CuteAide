#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import ctypes
from ctypes import wintypes

class MONITORINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.DWORD),
        ("rcMonitor", wintypes.RECT),
        ("rcWork", wintypes.RECT),
        ("dwFlags", wintypes.DWORD)
    ]

def get_monitor_info():
    monitors = []

    def monitor_enum_proc(hMonitor, hdcMonitor, lprcMonitor, dwData):
        info = {}
        monitor_info = MONITORINFO()
        monitor_info.cbSize = ctypes.sizeof(MONITORINFO)
        ctypes.windll.user32.GetMonitorInfoA(hMonitor, ctypes.byref(monitor_info))
        info['Monitor'] = (monitor_info.rcMonitor.left, monitor_info.rcMonitor.top, monitor_info.rcMonitor.right, monitor_info.rcMonitor.bottom)
        info['Flags'] = monitor_info.dwFlags
        monitors.append(info)
        return 1

    MonitorEnumProc = ctypes.WINFUNCTYPE(ctypes.c_int, wintypes.HMONITOR, wintypes.HDC, ctypes.POINTER(wintypes.RECT), wintypes.LPARAM)
    ctypes.windll.user32.EnumDisplayMonitors(None, None, MonitorEnumProc(monitor_enum_proc), 0)

    if len(monitors) == 0:
        raise Exception("未找到显示器信息")
    elif len(monitors) == 1:
        return {'width': monitors[0]['Monitor'][2] - monitors[0]['Monitor'][0], 'height': monitors[0]['Monitor'][3] - monitors[0]['Monitor'][1]}
    else:
        for monitor in enumerate(monitors):
            data = monitor[1]
            if data['Flags'] & 1:
                return {'width': data['Monitor'][2] - data['Monitor'][0], 'height': data['Monitor'][3] - data['Monitor'][1]}


if __name__ == '__main__':
    print(get_monitor_info())