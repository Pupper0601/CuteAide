#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import os
import sys
from pathlib import Path

# 定义全局变量
_abs_path = None


def project_path() -> str:
    global _abs_path

    if getattr(sys, 'frozen', False):
        _abs_path = sys._MEIPASS
        return _abs_path
    elif __file__:
        _abs_path = os.path.dirname(__file__)
        _path = _abs_path.split("CuteAide")[0] + "CuteAide"
        return _path.replace("\\", "/")



def path_conn(file_name: str = '') -> str:
    return str(project_path() + file_name)


if __name__ == '__main__':
    print(project_path())
