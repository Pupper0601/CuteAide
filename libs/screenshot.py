# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Author : Pupper
# # @Email  : pupper.cheng@gmail.com

import cv2
import mss
import numpy as np

from libs.global_variable import GDV
from libs.handle_image import ContrastImage
from tools.log import logger


def screen_capture_full():
    # 截取整个屏幕的屏幕截图
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # 获取主显示器的分辨率
        captured_frame = sct.grab(monitor)
        full_frame = np.array(captured_frame)
        full_frame = cv2.cvtColor(full_frame, cv2.COLOR_BGRA2BGR)
        GDV.global_screenshot = full_frame


def extract_region(full_frame, region):
    # 从整个屏幕截图中提取指定区域
    x, y, width, height = region
    cropped_frame = full_frame[y:y + height, x:x + width]
    if cropped_frame.size == 0:
        logger.error("截取的图像为空")
        return None
    return cropped_frame


def get_inventory():
    # 获取背包信息的屏幕截图
    inventory_place = GDV.CACHE["config"]["regions"]["inventory"]
    temp_img = extract_region(GDV.global_screenshot, inventory_place)

    res = ContrastImage("inventory", GDV.CACHE["inventory"]["ku"], temp_img).result  # 比较背包信息

    if len(res) > 0:
        logger.info(f"当前背包 ---> 打开状态")
        return True
    logger.info(f"当前不是背包界面, 无法识别")
    return False


def get_gun_position(gun_position):
    _position = GDV.CACHE["config"]["position"]
    _temp_img = extract_region(GDV.global_screenshot, _position[gun_position])
    res = ContrastImage(f"position_{gun_position}", GDV.CACHE["position"][gun_position], _temp_img).result
    if len(res) > 0:
        return True
    return False


def get_car():
    # 获取车辆信息的屏幕截图
    car_place = GDV.CACHE["config"]["regions"]["car"]
    temp_img = extract_region(GDV.global_screenshot, car_place)

    res = ContrastImage("car", GDV.CACHE["car"]["car"], temp_img).result  # 比较车辆信息

    if len(res) > 0:
        GDV.in_car = "yes"
    else:
        GDV.in_car = "no"


if __name__ == '__main__':
    # 示例用法
    # get_inventory()
    # print(get_inventory())
    pass
