#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import os
import cv2
import pyautogui

from image_comparison import current_equipment
from tools.paths import project_path


def take_screenshots(regions, save_paths):
    #  截取区域的屏幕截图并将其保存到save_paths
    for region, save_path in zip(regions, save_paths):
        img = pyautogui.screenshot(region=region)
        save_path = project_path() + "/temps/" + save_path
        img.save(save_path)



regions = [
    [1375,98,50,12],
    [1609, 123, 42, 15],
    [1338, 242, 40, 40],
    [1440, 242, 40, 40],
    [1762, 242, 40, 40],
    [1375,324,50,12],
    [1609, 350, 42, 15],
    [1338, 465, 40, 40],
    [1440, 465, 40, 40],
    [1762, 465, 40, 40]
]

screenshot_paths = [
    "gun_1.png",
    "scope_1.png",
    "muzzle_1.png",
    "grip_1.png",
    "stock_1.png",
    "gun_2.png",
    "scope_2.png",
    "muzzle_2.png",
    "grip_2.png",
    "stock_2.png",
]

folder_paths = [
    "../basic_data/1920_1080/weapons",
    "../basic_data/1920_1080/scopes",
    "../basic_data/1920_1080/muzzles",
    "../basic_data/1920_1080/grips",
    "../basic_data/1920_1080/stocks",
]

take_screenshots(regions, screenshot_paths)

print(current_equipment(project_path() + "/basic_data/1920_1080/weapons/", project_path() + "/temps/gun_1.png"))
print(current_equipment(project_path() + "/basic_data/1920_1080/scopes/", project_path() + "/temps/scope_1.png"))
print(current_equipment(project_path() + "/basic_data/1920_1080/muzzles/", project_path() + "/temps/muzzle_1.png"))
print(current_equipment(project_path() + "/basic_data/1920_1080/grips/", project_path() + "/temps/grip_1.png"))
print(current_equipment(project_path() + "/basic_data/1920_1080/stocks/", project_path() + "/temps/stock_1.png"))

print(current_equipment(project_path() + "/basic_data/1920_1080/weapons/", project_path() + "/temps/gun_2.png"))
print(current_equipment(project_path() + "/basic_data/1920_1080/scopes/", project_path() + "/temps/scope_2.png"))
print(current_equipment(project_path() + "/basic_data/1920_1080/muzzles/", project_path() + "/temps/muzzle_2.png"))
print(current_equipment(project_path() + "/basic_data/1920_1080/grips/", project_path() + "/temps/grip_2.png"))
print(current_equipment(project_path() + "/basic_data/1920_1080/stocks/", project_path() + "/temps/stock_2.png"))


