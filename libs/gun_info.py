#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from libs.global_variable import CACHE
from libs.handle_image import current_equipment
from libs.screenshot import gun_screenshots



class GunInfo:
    def __init__(self):
        self.gun_info = {}

    def get_gun_1(self):
        temp_lists = gun_screenshots()
        gun_1 = {}
        gun_2 = {}
        gun_1["weapon"] = current_equipment(CACHE["weapon"], temp_lists["weapon_1"])
        gun_1["scope"] = current_equipment(CACHE["scope"], temp_lists["scope_1"])
        gun_1["muzzle"] = current_equipment(CACHE["muzzle"], temp_lists["muzzle_1"])
        gun_1["grip"] = current_equipment(CACHE["grip"], temp_lists["grip_1"])
        gun_1["stock"] = current_equipment(CACHE["stock"], temp_lists["stock_1"])

        gun_2["weapon"] = current_equipment(CACHE["weapon"], temp_lists["weapon_2"])
        gun_2["scope"] = current_equipment(CACHE["scope"], temp_lists["scope_2"])
        gun_2["muzzle"] = current_equipment(CACHE["muzzle"], temp_lists["muzzle_2"])
        gun_2["grip"] = current_equipment(CACHE["grip"], temp_lists["grip_2"])
        gun_2["stock"] = current_equipment(CACHE["stock"], temp_lists["stock_2"])
        self.gun_info["gun_1"] = gun_1
        self.gun_info["gun_2"] = gun_2



