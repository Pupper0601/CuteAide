#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import pyautogui

def take_screenshots(regions, save_paths ):
    for region, save_path in zip(regions, save_paths):
        img = pyautogui.screenshot(region=region)
        img.save(save_path)

# 定义多个区域和保存路径
regions = [
    [1375,98,50,12],
    [1375,324,50,12],
]

save_paths = [
    "1.png",
    "2.png",
]

# 截取并保存截图
take_screenshots(regions, save_paths)
