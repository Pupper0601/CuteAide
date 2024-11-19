#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import sys
from pathlib import Path

# 定义全局变量
PROJECT_PATH = None


def project_path() -> str:
    global PROJECT_PATH
    if PROJECT_PATH is None:
        # 使用 sys.argv[0] 获取可执行文件路径
        PROJECT_PATH = str(Path(sys.argv[0]).parent).split("CuteAide")[0] + "CuteAide"
    return PROJECT_PATH.replace("\\", "/")


def path_conn(file_name: str = '') -> str:
    return str(project_path() + file_name)


if __name__ == '__main__':
    print(project_path())
