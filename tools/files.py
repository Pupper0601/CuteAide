#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
from pathlib import Path

from paths import path_conn


def read_file(file_name: str) -> str:
    file_name = path_conn(file_name)
    if Path(file_name).exists():
        with open(file_name, 'r') as f:
            return f.read()
    else:
        return ''


def write_file(file_name: str, content: str) -> None:
    file_name = path_conn(file_name)
    # 文件如果存在则覆盖，不存在则创建
    with open(file_name, 'w+') as f:
        f.write(content)
