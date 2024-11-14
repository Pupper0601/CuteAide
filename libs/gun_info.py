#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from libs.global_variable import global_variable
from libs.global_variable import CACHE, THREAD_POOL, TRANSLATE
from libs.handle_image import current_equipment
from libs.screenshot import gun_screenshots



class GetGunInfo:
    def __init__(self):
        self.get_gun()

    @staticmethod
    def get_gun():
        temp_lists = gun_screenshots()
        gun_1 = {}
        gun_2 = {}
        if len(temp_lists) > 0:
            futures = {
                "weapon_1": THREAD_POOL.submit(current_equipment, CACHE["weapons"], temp_lists["weapon_1"]),
                "scope_1" : THREAD_POOL.submit(current_equipment, CACHE["scopes"], temp_lists["scope_1"]),
                "muzzle_1": THREAD_POOL.submit(current_equipment, CACHE["muzzles"], temp_lists["muzzle_1"]),
                "grip_1"  : THREAD_POOL.submit(current_equipment, CACHE["grips"], temp_lists["grip_1"]),
                "stock_1" : THREAD_POOL.submit(current_equipment, CACHE["stocks"], temp_lists["stock_1"]),
                "weapon_2": THREAD_POOL.submit(current_equipment, CACHE["weapons"], temp_lists["weapon_2"]),
                "scope_2" : THREAD_POOL.submit(current_equipment, CACHE["scopes"], temp_lists["scope_2"]),
                "muzzle_2": THREAD_POOL.submit(current_equipment, CACHE["muzzles"], temp_lists["muzzle_2"]),
                "grip_2"  : THREAD_POOL.submit(current_equipment, CACHE["grips"], temp_lists["grip_2"]),
                "stock_2" : THREAD_POOL.submit(current_equipment, CACHE["stocks"], temp_lists["stock_2"]),
            }

            results = {key: future.result() for key, future in futures.items()}

            gun_1["weapon"] = results["weapon_1"]
            gun_1["scope"] = results["scope_1"]
            gun_1["muzzle"] = results["muzzle_1"]
            gun_1["grip"] = results["grip_1"]
            gun_1["stock"] = results["stock_1"]

            gun_2["weapon"] = results["weapon_2"]
            gun_2["scope"] = results["scope_2"]
            gun_2["muzzle"] = results["muzzle_2"]
            gun_2["grip"] = results["grip_2"]
            gun_2["stock"] = results["stock_2"]

            for key, value in gun_1.items():
                gun_1[key] = [TRANSLATE[value], value]
            for key, value in gun_2.items():
                gun_2[key] = [TRANSLATE[value], value]

            global_variable.weapon_information = {"gun_1": gun_1, "gun_2": gun_2}

        # {'gun_1': {'weapon': ['自动装填步枪', 'ZDZT'], 'scope': ['6倍镜', 'x6'], 'muzzle': ['无枪口', 'muzzle_none'],
        #            'grip'  : ['无握把', 'grip_none'], 'stock': ['托腮板', 'tosaiban']},
        #  'gun_2': {'weapon': ['无武器', 'weapon_none'], 'scope': ['无倍镜', 'scope_none'],
        #            'muzzle': ['无枪口', 'muzzle_none'], 'grip': ['无握把', 'grip_none'],
        #            'stock' : ['无枪托', 'stock_none']}}


if __name__ == '__main__':
    gun = GunInfo()
    print(gun.gun_info)



