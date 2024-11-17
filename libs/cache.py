#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import json
from pathlib import Path

from libs.handle_image import ReadImage
from libs.monitor import get_monitor_info
from tools.paths import path_conn
from tools.log import logger

monitor = get_monitor_info()

# 定义全局变量

class ImageCache:
    def __init__(self):
        self.source_data = {}
        self.basic_path = Path(path_conn(f"/basic/{monitor['width']}_{monitor['height']}"))
        if len(self.source_data) == 0:
            self._read_weapons()
            self._read_scopes()
            self._read_muzzles()
            self._read_grips()
            self._read_stocks()
            self._read_config()
            self._read_car()
            self._read_inventory()
            self._read_shoot()
            self._read_poses()
            self._read_position()
            logger.info('源图缓存初始化完成')

    def _read_images(self, category):
        # 读取指定类别的图片
        category_path = self.basic_path / category  #   获取文件夹路径
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
        images = {}
        for file in category_path.iterdir():    #   遍历文件夹
            if file.suffix.lower() in image_extensions: #   判断是否是图片
                data = ReadImage(str(file))    #   读取图片
                images[file.stem] = [data.binary, data.pyramid]   #  将图片数据存入字典
        self.source_data[category] = images   #   将图片字典存入全局变量

    def _read_weapons(self):
        # 读取武器图片
        self._read_images('weapons')

    def _read_scopes(self):
        # 读取瞄准镜图片
        self._read_images('scopes')

    def _read_muzzles(self):
        # 读取枪口图片
        self._read_images('muzzles')

    def _read_grips(self):
        # 读取握把图片
        self._read_images('grips')

    def _read_stocks(self):
        # 读取枪托图片
        self._read_images('stocks')

    def _read_car(self):
        # 读取载具图片
        self._read_images('car')

    def _read_inventory(self):
        # 读取背包图片
        self._read_images('inventory')

    def _read_shoot(self):
        # 读取附近图片
        self._read_images('shoot')

    def _read_poses(self):
        # 读取姿势图片
        self._read_images('poses')

    def _read_position(self):
        # 读取姿势图片
        self._read_images('position')

    def _read_config(self):
        config_path= self.basic_path / 'config.json'
        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = json.load(file)
            self.source_data['config'] = self.config



if __name__ == '__main__':
    print(ImageCache().source_data)
    print(ImageCache().source_data)
    print(ImageCache().source_data)
