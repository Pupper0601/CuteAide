# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Author : Pupper
# # @Email  : pupper.cheng@gmail.com
import time

import cv2
import mss
import numpy as np

from libs.global_variable import GDV, THREAD_POOL
from libs.handle_image import ContrastImage
from tools.log import logger

def screen_capture_full():
    # 截取整个屏幕的屏幕截图
    with mss.mss() as sct:
        start_time = time.time()
        monitor = sct.monitors[1]  # 获取主显示器的分辨率
        captured_frame = sct.grab(monitor)  # 截取整个屏幕的屏幕截图
        full_frame = np.array(captured_frame)
        full_frame = cv2.cvtColor(full_frame, cv2.COLOR_BGRA2BGR)

        # 获取当前分辨率
        current_resolution = (full_frame.shape[1], full_frame.shape[0])
        target_resolution = (1920, 1080)

        # 如果当前分辨率不是1920x1080，则进行转换
        if current_resolution != target_resolution:
            resized_frame = cv2.resize(full_frame, target_resolution, interpolation=cv2.INTER_AREA)
        else:
            resized_frame = full_frame

        GDV.global_screenshot = resized_frame

        logger.info(f"截取整个屏幕的屏幕截图耗时: {time.time() - start_time:.2f}秒")

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
    screen_capture_full()  # 截取整个屏幕的屏幕截图
    inventory_place = GDV.CACHE["config"]["regions"]["inventory"]
    temp_img = extract_region(GDV.global_screenshot, inventory_place)

    res = ContrastImage("inventory", GDV.CACHE["inventory"]["ku"], temp_img).result  # 比较背包信息

    if len(res) > 0:
        logger.info(f"当前背包 ---> 打开状态")
        GDV.enable_mouse_recognition = True
        GDV.enable_key_recognition = False
        return True
    logger.info(f"当前不是背包界面, 无法识别")
    GDV.enable_key_recognition = True
    GDV.enable_mouse_recognition = False
    return False


def get_gun_position(gun_position):
    # 获取枪械位置
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

def get_shooting_state():
    # 获取射击状态
    screen_capture_full()   # 截取整个屏幕的屏幕截图
    shooting_state_place = GDV.CACHE["config"]["shooting_state"]

    for key, value in shooting_state_place.items():
        temp_img = extract_region(GDV.global_screenshot, value) # 从整个屏幕截图中提取指定区域
        if check_near_white_pixels(temp_img):   # 检查图像中是否有连续10个像素的颜色接近于白色
            GDV.shooting_state = "fired"
            logger.info(f"当前射击状态 --->>> 开火, {GDV.shooting_state}")
            return True
    return False

def check_near_white_pixels(image):
    # 检查图像中是否有连续10个像素的颜色接近于白色
    white_threshold = 200  # 定义接近白色的阈值
    for row in image:
        count = 0
        for pixel in row:
            if all(channel >= white_threshold for channel in pixel):
                count += 1
                if count == 50:
                    return True
            else:
                count = 0
    return False

if __name__ == '__main__':
    # 示例用法
    # get_inventory()
    # print(get_inventory())
    pass
