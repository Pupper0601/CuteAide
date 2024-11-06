#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pathlib import Path

from libs.screen_resolution import get_monitor_info
from tools.paths import path_conn
from libs.cache import ImageCache


def resolution():
    reso = get_monitor_info()
    sources = path_conn(f"/basic/{reso['width']}_{reso['height']}")
    if Path(sources):
        ImageCache()   #   读取图片
        return {'state': "已适配", 'resolution':f" {reso['width']}x{reso['height']}"}
    else:
        return {'state': "未适配", 'resolution':f" {reso['width']}x{reso['height']}"}


if __name__ == '__main__':
    print(resolution())