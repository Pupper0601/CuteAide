#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from libs.global_variable import CACHE
from libs.handle_image import current_equipment
from libs.screenshot import gun_screenshots



class GunInfo:
    def __init__(self):
        self.gun_info = None

    def get_gun_1(self):
        temp_lists = gun_screenshots()
        current_equipment("weapon")
        pass

    def _weapon(self):
        current_equipment("weapon")



