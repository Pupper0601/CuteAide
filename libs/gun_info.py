#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time

from libs.global_variable import global_variable
from libs.global_variable import CACHE, THREAD_POOL, TRANSLATE
from libs.handle_image import current_equipment
from libs.screenshot import extract_region, get_gun_position
from tools.log import logger


class GetGunInfo:
    def __init__(self):
        start_tiem = time.time()
        self.get_gun()
        logger.info(f"获取枪械信息耗时: {time.time() - start_tiem}")

    @staticmethod
    def get_gun():
        gun_1 = {}
        gun_2 = {}
        _position = CACHE["config"]["regions"]
        _full_frame = global_variable.global_screenshot
        if get_gun_position("1"):
            futures_1 = {
                "weapon_1": THREAD_POOL.submit(current_equipment,"weapon", CACHE["weapons"], extract_region(_full_frame,
                                                                                                            _position[
                                                                                                                 "weapon_1"])),
                "scope_1" : THREAD_POOL.submit(current_equipment,"scope", CACHE["scopes"], extract_region(_full_frame,_position[
                                                                                                                        "scope_1"])),
                "muzzle_1": THREAD_POOL.submit(current_equipment,"muzzle", CACHE["muzzles"], extract_region(_full_frame,_position[
                                                                                                                 "muzzle_1"])),
                "grip_1"  : THREAD_POOL.submit(current_equipment,"grip", CACHE["grips"], extract_region(_full_frame,_position[
                                                                                                               "grip_1"])),
                "stock_1" : THREAD_POOL.submit(current_equipment,"stock", CACHE["stocks"], extract_region(_full_frame,_position[
                                                                                                                "stock_1"]))}
            results_1 = {key: future.result() for key, future in futures_1.items()}

            gun_1["weapon"] = results_1["weapon_1"]
            gun_1["scope"] = results_1["scope_1"]
            gun_1["muzzle"] = results_1["muzzle_1"]
            gun_1["grip"] = results_1["grip_1"]
            gun_1["stock"] = results_1["stock_1"]

        if get_gun_position("2"):
            futures_2 = {
                "weapon_2": THREAD_POOL.submit(current_equipment,"weapon", CACHE["weapons"], extract_region(_full_frame,_position[
                                                                                                                 "weapon_2"])),
                "scope_2" : THREAD_POOL.submit(current_equipment,"scope", CACHE["scopes"], extract_region(_full_frame,_position[
            "scope_2"])),
                "muzzle_2": THREAD_POOL.submit(current_equipment,"muzzle", CACHE["muzzles"], extract_region(_full_frame,_position[
        "muzzle_2"])),
                "grip_2"  : THREAD_POOL.submit(current_equipment,"grip", CACHE["grips"], extract_region(_full_frame,_position[
                                                                                                               "grip_2"])),
                "stock_2" : THREAD_POOL.submit(current_equipment,"stock", CACHE["stocks"], extract_region(_full_frame,_position[                                                                                                    "stock_2"]))
            }

            results_2 = {key: future.result() for key, future in futures_2.items()}

            gun_2["weapon"] = results_2["weapon_2"]
            gun_2["scope"] = results_2["scope_2"]
            gun_2["muzzle"] = results_2["muzzle_2"]
            gun_2["grip"] = results_2["grip_2"]
            gun_2["stock"] = results_2["stock_2"]

        if len(gun_1) > 0:
            for key, value in gun_1.items():
                gun_1[key] = [TRANSLATE[value], value]
        else:
            gun_1 = {"weapon": ["无武器", "weapon_none"], "scope": ["无倍镜", "scope_none"],
                     "muzzle": ["无枪口", "muzzle_none"], "grip": ["无握把", "grip_none"],
                     "stock" : ["无枪托", "stock_none"]}
        if len(gun_2) > 0:
            for key, value in gun_2.items():
                gun_2[key] = [TRANSLATE[value], value]
        else:
            gun_2 = {"weapon": ["无武器", "weapon_none"], "scope": ["无倍镜", "scope_none"],
                     "muzzle": ["无枪口", "muzzle_none"], "grip": ["无握把", "grip_none"],
                     "stock" : ["无枪托", "stock_none"]}

        global_variable.weapon_information = {"gun_1": gun_1, "gun_2": gun_2}

        # {'gun_1': {'weapon': ['自动装填步枪', 'ZDZT'], 'scope': ['6倍镜', 'x6'], 'muzzle': ['无枪口', 'muzzle_none'],
        #            'grip'  : ['无握把', 'grip_none'], 'stock': ['托腮板', 'tosaiban']},
        #  'gun_2': {'weapon': ['无武器', 'weapon_none'], 'scope': ['无倍镜', 'scope_none'],
        #            'muzzle': ['无枪口', 'muzzle_none'], 'grip': ['无握把', 'grip_none'],
        #            'stock' : ['无枪托', 'stock_none']}}


if __name__ == '__main__':
    gun = GetGunInfo()
    print(global_variable.weapon_information)



