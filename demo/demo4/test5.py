#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import win32gui
import win32process
import psutil


def get_active_window_info():

    hwnd = win32gui.GetForegroundWindow()  # 获取当前活动窗口句柄


    _, pid = win32process.GetWindowThreadProcessId(hwnd)  # 获取窗口对应的进程ID


    process = psutil.Process(pid)  # 获取进程信息


    window_title = win32gui.GetWindowText(hwnd)  # 获取窗口标题


    process_name = process.name()  # 获取进程名称


    return {


        "window_title": window_title,


        "process_name": process_name,


        "pid": pid


    }


if __name__ == "__main__":


    active_window_info = get_active_window_info()


    print(active_window_info)