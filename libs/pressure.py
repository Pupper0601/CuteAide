#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import json
from pathlib import Path

from libs.global_variable import GDV, THREAD_POOL
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
        current_weapon_info = GDV.current_weapon_information
        # {'weapon': ['SKS', 'SKS'], 'scope': ['6倍镜', 'x6'], 'muzzle': ['消音器', 'xiaoyin-b'],'grip'  : ['轻型握把',
        # 'qingxin'], 'stock': ['托腮板', 'tosaiban']}

        if current_weapon_info:
            _weapon_name = current_weapon_info["weapon"][1]
            # 获取当前武器名称
            _factor_data["weapon"] = _weapon_name

            # 获取当前武器的配件系数
            _components = _gun_data["component_factor"]
            if _weapon_name in _components.keys():
                _factors = _components[_weapon_name]

                for key, value in current_weapon_info.items():  # 'scope',  ['红点瞄准镜', 'hongdian']
                    if key != "weapon":
                        try:
                            if key == "scope":
                                _factor_data["magnifying_power"] = _gun_data["global_magnifying_power"][value[1]]
                            _factor_data[key] = _factors[key][value[1]]
                        except KeyError:
                            logger.error(f"配件系数中没有找到对应的配件: {value[1]}")
                            _factor_data[key] = 1.0

                _factor_data["car"] = _factors["car"]["car"]
                # 获取当前姿态
                _factor_data["posture_state"] = _factors["pose"][GDV.posture_state]

                # 获取当前武器基础系数
                if _weapon_name in _gun_data["alone_factor"].keys():
                    _factor_data["alone_factor"] = _gun_data["alone_factor"][_weapon_name]

                # 获取当前武器射击间隔
                if _weapon_name in _gun_data["weapon_intervals"].keys():
                    _factor_data["weapon_intervals"] = _gun_data["weapon_intervals"][_weapon_name]

                # 获取当前武器弹道
                if _weapon_name in _gun_data["guns_trajectory"].keys():
                    _factor_data["guns_trajectory"] = _gun_data["guns_trajectory"][_weapon_name]["default"]
            else:
                _factor_data["no_gun"] = True

            # 获取是否上车
            _factor_data["in_car"] = GDV.in_car

            # 获取武器射击状态
            _factor_data["shooting_state"] = GDV.shooting_state

            # 开镜方式
            _factor_data["opening_method"] = GDV.opening_method

            # 获取全局 shift 系数
            _factor_data["global_lshift"] = _gun_data["global_lshift"]

            # 获取全局后坐力系数
            _factor_data["global_recoil"] = _gun_data["global_recoil"]

            logger.info(f"当前武器: {_factor_data}")
            return _factor_data

    def calculate_factors(self):
        _effect_data = self.get_component_factor()
        if _effect_data is not None:
            if not _effect_data.get("no_gun"):
                coefficient = 1.0
                coefficient *= _effect_data["posture_state"]  # 姿态系数
                coefficient *= _effect_data["scope"]  # 瞄准镜系数
                coefficient *= _effect_data["muzzle"]  # 枪口系数
                coefficient *= _effect_data["grip"]  # 握把系数
                coefficient *= _effect_data["stock"]  # 枪托系数
                coefficient *= _effect_data["global_recoil"]  # 全局后坐力系数
                coefficient *= _effect_data["alone_factor"]  # 武器基础系数
                coefficient *= _effect_data["magnifying_power"]  # 瞄准镜倍数

                del _effect_data["posture_state"]  # 删除字典中的姿态系数
                del _effect_data["scope"]
                del _effect_data["muzzle"]
                del _effect_data["grip"]
                del _effect_data["stock"]
                del _effect_data["global_recoil"]
                del _effect_data["alone_factor"]
                del _effect_data["magnifying_power"]

                _effect_data["coefficient"] = coefficient

                return _effect_data
            else:
                _effect_data["coefficient"] = "none"
                return _effect_data

    def write_dict_to_lua_file(self):
        file_path = "C:/CuteAide/output.lua"
        path = Path(file_path)
        if not path.is_file():
            # 如果文件夹不存在，则创建
            path.parent.mkdir(parents=True, exist_ok=True)
            # 创建文件
            path.touch()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.truncate(0)  # 清空文件内容
            _gun_info = self.calculate_factors()
            if _gun_info is not None:
                for key, value in _gun_info.items():
                    if isinstance(value, str):
                        file.write(f"{key} = '{value}'\n")
                    elif isinstance(value, list):
                        if key == "guns_trajectory":
                            formatted_list = ", ".join([f"{{{i + 1}, {v}}}" for i, v in enumerate(value)])
                            file.write(f"{key} = {{{formatted_list}}}\n")
                    else:
                        file.write(f"{key} = {value}\n")


if __name__ == '__main__':
    a = {'weapon': ['Beryl M762', 'M762'], 'scope': ['红点瞄准镜', 'hongdian'], 'muzzle': ['后座补偿器', 'buchang-b'],
         'grip'  : ['垂直握把', 'chuizhi'], 'stock': ['无枪托', 'stock_none']}
    # p = Pressure(a)
