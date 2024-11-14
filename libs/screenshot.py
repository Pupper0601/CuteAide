# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Author : Pupper
# # @Email  : pupper.cheng@gmail.com

import pyautogui

from libs.global_variable import global_variable
from libs.global_variable import CACHE, THREAD_POOL
from libs.handle_image import ContrastImage
from tools.paths import project_path
from tools.log import logger


def screen_capture(region, name):
    #  截取区域的屏幕截图并将其保存到save_path
    img = pyautogui.screenshot(region=region)
    save_path = project_path() + "/temps/" + name
    img.save(save_path)
    return save_path    # 返回保存路径

def get_inventory():
    # 获取背包信息的屏幕截图
    inventory_place = CACHE["config"]["regions"]["inventory"]
    temp_path= screen_capture(inventory_place, "inventory.png")

    res = ContrastImage("inventory", CACHE["inventory"]["ku"], temp_path).result  # 比较背包信息

    if len(res) > 0:
        logger.info(f"当前背包 ---> 打开状态")
        return True
    logger.info(f"当前不是背包界面, 无法识别")
    return False


def gun_screenshots():
    # 截取装备信息的屏幕截图
    paths_dict = {}
    gun_sites = CACHE["config"]  # 获取装备信息

    if get_inventory(): # 如果是背包界面

        for key, value in gun_sites['regions'].items():
            if key not in ["inventory", "car", "pose"]:
                paths_dict[key] = screen_capture(value, key + ".png")

        logger.info("装备获取图截取 ---> 完成")
        return paths_dict   # {文件名: 路径, ...}
    else:
        logger.info("装备获取图截取 ---> 失败")
        return paths_dict

def get_car():
    # 获取车辆信息的屏幕截图
    car_place = CACHE["config"]["regions"]["car"]
    temp_path = screen_capture(car_place, "car.png")

    res = ContrastImage("car", CACHE["car"]["car"], temp_path).result  # 比较车辆信息

    if len(res) > 0:
        global_variable.in_car = "yes"
    else:
        global_variable.in_car = "no"


if __name__ == '__main__':
    # 示例用法
    screen_capture([0, 0, 100, 100], "test.png")
    print(gun_screenshots())
