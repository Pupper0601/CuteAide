#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import importlib
import json

from libs.global_variable import global_variable
from libs.global_variable import THREAD_POOL
from tools.files import read_file
from tools.log import logger


class Pressure:
    def __init__(self):
        # self.s = weapon_info
        THREAD_POOL.submit(self.write_dict_to_lua_file())

    @staticmethod
    def get_component_factor():

        _gun_data = json.loads(read_file("/gun_data.json"))

        _factor_data = {}
        _calculate_coefficient = 1.0

        gun_data = importlib.reload(importlib.import_module('libs.gun_data'))   # 重新加载 gun_data 模块以确保获取最新数据
        current_weapon_info = global_variable.current_weapon_information
        # {'weapon': ['SKS', 'SKS'], 'scope': ['6倍镜', 'x6'], 'muzzle': ['消音器', 'xiaoyin-b'],'grip'  : ['轻型握把', 'qingxin'], 'stock': ['托腮板', 'tosaiban']}

        if current_weapon_info:
            _weapon_name = current_weapon_info["weapon"][1]
            # 获取当前武器名称
            _factor_data["weapon"] = _weapon_name

            if _weapon_name in gun_data.component_factor.keys():
                _factors = gun_data.component_factor[_weapon_name]

                for key, value in current_weapon_info.items():  # 'scope',  ['红点瞄准镜', 'hongdian']
                    if key != "weapon":
                        try:
                            if key == "scope":
                                _calculate_coefficient *= gun_data.global_magnifying_power[value[1]]
                            _calculate_coefficient *= _factors[key][value[1]]
                        except KeyError:
                            logger.error(f"配件系数中没有找到对应的配件: {value[1]}")
                            _calculate_coefficient *= 1.0

                _factor_data["car"] = _factors["car"]["car"]
                # 获取当前姿态
                _factor_data["posture_state"] = _factors["pose"][global_variable.posture_state]

            # 获取是否上车
            _factor_data["in_car"] = global_variable.in_car

            # 获取当前武器弹道
            if _weapon_name in _gun_data["guns_trajectory"].keys():
                _factor_data["guns_trajectory"] = _gun_data["guns_trajectory"][_weapon_name]["default"]
            else:
                _factor_data["guns_trajectory"] = _gun_data["guns_trajectory"]["weapon_none"]["default"]

            # 获取当前武器射击间隔
            if _weapon_name in _gun_data["weapon_intervals"].keys():
                _factor_data["weapon_intervals"] = _gun_data["weapon_intervals"][_weapon_name]
            else:
                _factor_data["weapon_intervals"] = _gun_data["weapon_intervals"]["weapon_none"]

            # 获取武器射击状态
            _factor_data["shooting_state"] = global_variable.shooting_state

            # 开镜方式
            _factor_data["opening_method"] = global_variable.opening_method

            # 获取当前武器基础系数
            if _weapon_name in _gun_data["alone_factor"].keys():
                _calculate_coefficient *= _gun_data["alone_factor"][_weapon_name]
            else:
                _calculate_coefficient *= 1.0

            # 获取全局 shift 系数
            _factor_data["global_lshift"] = _gun_data["global_lshift"]

            # 获取全局后坐力系数
            _calculate_coefficient *= _gun_data["global_recoil"]

            # 获取垂直后坐力
            _calculate_coefficient *= _gun_data["global_vertical"]

            _factor_data["coefficient"] = _calculate_coefficient

            return _factor_data

    def write_dict_to_lua_file(self):
        paths = r"F:\Object\GitHub\CuteAide\output.lua"
        with open(paths, 'w', encoding='utf-8') as file:
            file.truncate(0)    # 清空文件内容
            _gun_info = self.get_component_factor()
            if _gun_info is not None:
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
    # p = Pressure(a)





