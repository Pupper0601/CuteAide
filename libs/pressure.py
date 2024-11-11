#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from libs.gun_data import alone_factor, global_recoil, component_factor, guns_trajectory,weapon_intervals, global_lshift
from tools.log import logger
from tools.paths import path_conn


class Pressure:
    def __init__(self, gun_info: dict, pose, shoot):
        self.guns_info = gun_info
        self.pose = pose
        self.shoot = shoot
        self.gun_1 = {}
        self.gun_2 = {}
        self.pose = "stand"
        self.get_gun_data()

    def get_gun_data(self):
        if self.guns_info is not None:
            for key, value in self.guns_info.items():
                if key == "gun_1":
                    self.gun_1.update({"weapon": value["weapon"][1]})
                    self.gun_1.update(self.get_gun_factor(value))
                    self.gun_1.update(self.get_component_factor(value))
                    self.gun_1.update(self.get_guns_trajectory(value))
                    self.gun_1.update(self.get_weapon_intervals(value))
                    self.gun_1.update({"global_recoil": global_recoil})
                    self.gun_1.update({"global_lshift": global_lshift})
                    self.gun_1.update({"shoot": self.shoot})
                elif key == "gun_2":
                    self.gun_2.update({"weapon": value["weapon"][1]})
                    self.gun_2.update(self.get_gun_factor(value))
                    self.gun_2.update(self.get_component_factor(value))
                    self.gun_2.update(self.get_guns_trajectory(value))
                    self.gun_2.update(self.get_weapon_intervals(value))
                    self.gun_2.update({"global_recoil": global_recoil})
                    self.gun_2.update({"global_lshift": global_lshift})
                    self.gun_1.update({"shoot": self.shoot})

    @staticmethod
    def get_gun_factor(gun_info: dict):
        return {"alone_factor": alone_factor[gun_info["weapon"][1]]}

    def get_component_factor(self, gun_info: dict):
        _factor_data = {}
        _factors = component_factor[gun_info["weapon"][1]]
        for key, value in gun_info.items():
            if key in _factors.keys():
                for k,v in _factors[key].items():
                    if k == value[1]:
                        _factor_data[key] = v
            elif key != "weapon":
                _factor_data[key] = 1.0
        _factor_data["pose"] = _factors["pose"][self.pose]
        _factor_data.update(_factors["car"])
        return _factor_data

    @staticmethod
    def get_guns_trajectory(gun_info: dict):
        return {"guns_trajectory": guns_trajectory[gun_info["weapon"][1]]["default"]}

    @staticmethod
    def get_weapon_intervals(gun_info: dict):
        return {"weapon_intervals": weapon_intervals[gun_info["weapon"][1]]}

    def write_dict_to_lua_file(self):
        if self.shoot == "1":
            gun = self.gun_1
        elif self.shoot == "2":
            gun = self.gun_2
        else:
            gun = self.gun_1
        logger.info(f"写入枪械数据到文件: {gun}")
        paths = path_conn('/output.lua')
        with open(paths, 'w', encoding='utf-8') as file:
            for key, value in gun.items():
                if isinstance(value, str):
                    file.write(f"{key} = '{value}',\n")
                elif isinstance(value, list):
                    file.write(f"{key} = {{{', '.join(map(str, value))}}},\n")
                else:
                    file.write(f"{key} = {value},\n")



if __name__ == '__main__':
    a = {'gun_1': {'weapon': ['M416', 'M416'], 'scope': ['红点瞄准镜', 'hongdian'], 'muzzle': ['后座补偿器', 'buchang-b'], 'grip': ['垂直握把', 'chuizhi'], 'stock': ['战术枪托', 'zhanshu']}, 'gun_2': {'weapon': ['SKS', 'SKS'], 'scope': ['6倍镜', 'x6'], 'muzzle': ['消音器', 'xiaoyin-b'], 'grip': ['轻型握把', 'qingxin'], 'stock': ['托腮板', 'tosaiban']}}
    p = Pressure(a)




