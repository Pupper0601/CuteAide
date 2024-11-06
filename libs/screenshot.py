# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Author : Pupper
# # @Email  : pupper.cheng@gmail.com
from concurrent.futures import ThreadPoolExecutor

import pyautogui
from PySide6.QtCore import QObject, Signal

from .comparison import current_equipment
from tools.paths import project_path
from libs.cache import ImageCache
from tools.log import logger


def take_screenshots(region, save_path):
    #  截取区域的屏幕截图并将其保存到save_path
    img = pyautogui.screenshot(region=region)
    save_path = project_path() + "/temps/" + save_path
    img.save(save_path)
    return save_path

def gun_screenshots():
    #   截取装备信息的屏幕截图
    paths_dict = {}
    gun_sites = ImageCache.source_data["config"]   # 获 取装备信息

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(take_screenshots, value, key + ".png"): key for key, value in
                   gun_sites['regions'].items()}
        for future in futures:
            key = futures[future]
            paths_dict[key] = future.result()

    logger.info("截图完成")
    return paths_dict


class GetGunInfo(QObject):
    gun_info_signal = Signal(dict)  # 定义信号, 传递装备信息

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.temp_images = gun_screenshots()
        self.gun_cache = ImageCache.source_data
        self.gun_1 = {}
        self.gun_2 = {}
        self.get_gun_1()
        self.get_gun_2()
        logger.info(self.gun_1)
        logger.info(self.gun_2)
        self.emit_gun_info()  # 发送信号
        self.parent.update_gun_info(self.gun_1, self.gun_2)  # 调用 update_gun_info 方法


    def get_gun_1(self):
        # 获取武器1的装备信息
        equip_data = self.gun_cache['equip']
        with ThreadPoolExecutor() as executor:
            futures = {
                "weapon": executor.submit(current_equipment, self.gun_cache['weapons'],
                                          self.temp_images["weapon_name_1"]),
                "scope" : executor.submit(current_equipment, self.gun_cache['scopes'], self.temp_images[
                    "scope_1"]),
                "muzzle": executor.submit(current_equipment, self.gun_cache['muzzles'], self.temp_images[
                    "muzzle_1"]),
                "grip"  : executor.submit(current_equipment, self.gun_cache['grips'], self.temp_images[
                    "grip_1"]),
                "stock" : executor.submit(current_equipment, self.gun_cache['stocks'], self.temp_images[
                    "stock_1"])
            }
            for key, future in futures.items():
                self.gun_1[key] = equip_data[future.result()]

    def get_gun_2(self):
        # 获取武器2的装备信息
        equip_data = self.gun_cache['equip']
        with ThreadPoolExecutor() as executor:
            futures = {
                "weapon": executor.submit(current_equipment, self.gun_cache['weapons'],
                                          self.temp_images["weapon_name_2"]),
                "scope" : executor.submit(current_equipment, self.gun_cache['scopes'], self.temp_images[
                    "scope_2"]),
                "muzzle": executor.submit(current_equipment, self.gun_cache['muzzles'], self.temp_images[
                    "muzzle_2"]),
                "grip"  : executor.submit(current_equipment, self.gun_cache['grips'], self.temp_images[
                    "grip_2"]),
                "stock" : executor.submit(current_equipment, self.gun_cache['stocks'], self.temp_images[
                    "stock_2"])
            }
            for key, future in futures.items():
                self.gun_2[key] = equip_data[future.result()]

    def emit_gun_info(self):
        # 发送枪械信息信号
        gun_info = {
            "gun_1": self.gun_1,
            "gun_2": self.gun_2
        }
        self.gun_info_signal.emit(gun_info) # 发送信号
