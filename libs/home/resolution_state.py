#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pathlib import Path

from libs.cache import ImageCache
from libs.global_variable import GDV
from libs.monitor import get_monitor_info
from tools.paths import path_conn


def resolution():
    reso = get_monitor_info()
    sources = path_conn(f"/basic/{reso['width']}_{reso['height']}")
    if Path(sources):
        GDV.CACHE = ImageCache().source_data
        return {'state': "已适配", 'resolution': f" {reso['width']}x{reso['height']}"}
    else:
        return {'state': "未适配", 'resolution': f" {reso['width']}x{reso['height']}"}


if __name__ == '__main__':
    print(resolution())
