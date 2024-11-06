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

resolution = None

def get_monitor_info():
    # 获取显示器信息，如果只有一个显示器，则返回该显示器的分辨率，如果有多个显示器，则返回主显示器的分辨率
    global resolution
    monitors = []
    if resolution is None:
        def monitor_enum_proc(hMonitor, hdcMonitor, lprcMonitor, dwData):
            info = {}
            monitor_info = MONITORINFO()
            monitor_info.cbSize = ctypes.sizeof(MONITORINFO)
            ctypes.windll.user32.GetMonitorInfoA(hMonitor, ctypes.byref(monitor_info))
            info['Monitor'] = (monitor_info.rcMonitor.left, monitor_info.rcMonitor.top, monitor_info.rcMonitor.right,
                               monitor_info.rcMonitor.bottom)
            info['Flags'] = monitor_info.dwFlags
            monitors.append(info)
            return 1

        MonitorEnumProc = ctypes.WINFUNCTYPE(ctypes.c_int, wintypes.HMONITOR, wintypes.HDC, ctypes.POINTER(wintypes.RECT),
                                             wintypes.LPARAM)
        ctypes.windll.user32.EnumDisplayMonitors(None, None, MonitorEnumProc(monitor_enum_proc), 0)

        if len(monitors) == 0:
            raise Exception("未找到显示器信息")
        elif len(monitors) == 1:
            resolution = {'width': monitors[0]['Monitor'][2] - monitors[0]['Monitor'][0],
                          'height': monitors[0]['Monitor'][3] - monitors[0]['Monitor'][1]}
            return resolution
        else:
            for monitor in enumerate(monitors):
                data = monitor[1]
                if data['Flags'] & 1:
                    resolution = {'width': data['Monitor'][2] - data['Monitor'][0],
                                  'height': data['Monitor'][3] - data['Monitor'][1]}
                    return resolution
    return resolution

if __name__ == '__main__':
    print(get_monitor_info())
