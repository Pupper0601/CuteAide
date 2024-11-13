#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from libs import global_variable
from libs.global_variable import THREAD_POOL
from libs.gun_data import *
from tools.log import logger
from tools.paths import path_conn


class Pressure:
    def __init__(self):
        # self.s = weapon_info
        THREAD_POOL.submit(self.write_dict_to_lua_file())

    @staticmethod
    def get_component_factor():
        _factor_data = {}
        current_weapon_info = global_variable.current_weapon_information
        # current_weapon_info = self.s
        if current_weapon_info:
            _weapon_name = current_weapon_info["weapon"][1]

            # 获取当前武器名称
            _factor_data["weapon"] = _weapon_name

            # 获取当前武器配件系数
            if _weapon_name in component_factor.keys():
                _factors = component_factor[_weapon_name]
                for key, value in current_weapon_info.items():  # 'scope',  ['红点瞄准镜', 'hongdian']
                    if key in _factors.keys():
                        for k, v in _factors[key].items():
                            if value[1] in _factors[key].keys():
                                if k == value[1]:
                                    _factor_data[key] = v
                            else:
                                _factor_data[key] = 1.0
                    elif key != "weapon":
                        _factor_data[key] = 1.0
                _factor_data["car"] = _factors["car"]["car"]
                # 获取当前姿态
                _factor_data["posture_state"] = _factors["pose"][global_variable.posture_state]
            else:
                _factor_data["scope"] = 1.0
                _factor_data["muzzle"] = 1.0
                _factor_data["grip"] = 1.0
                _factor_data["stock"] = 1.0
                _factor_data["car"] = 1.0
                global_variable.shooting_state = "stop"

            # 获取是否上车
            _factor_data["in_car"] = global_variable.in_car

            # 获取当前武器弹道
            if _weapon_name in guns_trajectory.keys():
                _factor_data["guns_trajectory"] = guns_trajectory[_weapon_name]["default"]
            else:
                _factor_data["guns_trajectory"] = guns_trajectory["weapon_none"]["default"]

            # 获取当前武器射击间隔
            if _weapon_name in weapon_intervals.keys():
                _factor_data["weapon_intervals"] = weapon_intervals[_weapon_name]
            else:
                _factor_data["weapon_intervals"] = weapon_intervals["weapon_none"]

            # 获取武器射击状态
            _factor_data["shooting_state"] = global_variable.shooting_state

            # 开镜方式
            _factor_data["opening_method"] = global_variable.opening_method

            # 连点开关
            _factor_data["continuous_clicks"] = global_variable.continuous_clicks

            # 获取当前武器基础系数
            if _weapon_name in alone_factor.keys():
                _factor_data["alone_factor"] = alone_factor[_weapon_name]
            else:
                _factor_data["alone_factor"] = 1.0

            # 获取全局 shift 系数
            _factor_data["global_lshift"] = global_lshift

            # 获取全局后坐力系数
            _factor_data["global_recoil"] = global_recoil

            logger.info(f"当前武器系数: {_factor_data}")
            return _factor_data

    def write_dict_to_lua_file(self):
        paths = path_conn('/output.lua')
        with open(paths, 'w', encoding='utf-8') as file:
            for key, value in self.get_component_factor().items():
                if isinstance(value, str):
                    file.write(f"{key} = '{value}'\n")
                elif isinstance(value, list):
                    if key == "guns_trajectory":
                        formatted_list = ", ".join([f"{{{i + 1}, {v}}}" for i, v in enumerate(value)])
                        file.write(f"{key} = {{{formatted_list}}}\n")
                else:
                    file.write(f"{key} = {value}\n")


if __name__ == '__main__':
    a = {'weapon': ['Beryl M762', 'M762'], 'scope': ['红点瞄准镜', 'hongdian'], 'muzzle': ['后座补偿器', 'buchang-b'], 'grip': ['垂直握把', 'chuizhi'], 'stock': ['无枪托', 'stock_none']}
    p = Pressure(a)





