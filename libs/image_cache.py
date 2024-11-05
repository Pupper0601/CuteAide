#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import json
import os

import cv2

from tools.screen_resolution import get_monitor_info
from tools.paths import path_conn

resolution = get_monitor_info()

class ImageCache:
    def __init__(self):
        self.basic_path = path_conn(f"/basic/{resolution['width']}_{resolution['height']}")
        self.weapons = {}
        self.scopes = {}
        self.muzzles = {}
        self.grasps = {}
        self.stocks = {}
        self.config = {}
        self.car = {}
        self.inventory = {}
        self.shoot = {}
        self.poses = {}

    def _read_images(self, category):
        # 读取指定类别的图片
        category_path = self.basic_path + category  #   获取文件夹路径
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
        images = {}
        for file in category_path.iterdir():    #   遍历文件夹
            if file.suffix.lower() in image_extensions: #   判断是否是图片
                images[file.stem] = cv2.imread(str(file))   #   读取图片
        return images   #   返回图片字典

    def _read_weapons(self):
        # 读取武器图片
        self.weapons = self._read_images('weapons')

    def _read_scopes(self):
        # 读取瞄准镜图片
        self.scopes = self._read_images('scopes')

    def _read_muzzles(self):
        # 读取枪口图片
        self.muzzles = self._read_images('muzzles')

    def _read_grasps(self):
        # 读取握把图片
        self.grasps = self._read_images('grasps')

    def _read_stocks(self):
        # 读取枪托图片
        self.stocks = self._read_images('stocks')

    def _read_car(self):
        # 读取载具图片
        self.car = self._read_images('car')

    def _read_inventory(self):
        # 读取背包图片
        self.inventory = self._read_images('inventory')

    def _read_shoot(self):
        # 读取附近图片
        self.shoot = self._read_images('shoot')

    def _read_poses(self):
        # 读取姿势图片
        self.poses = self._read_images('poses')

    def _read_config(self):
        config_path= self.basic_path + '/config.json'
        with open('config_path', 'r', encoding='utf-8') as file:
            self.config = json.load(file)

