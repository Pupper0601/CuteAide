#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pathlib import Path

# 定义全局变量
PROJECT_PATH = None

def project_path() -> str:
    global PROJECT_PATH
    if PROJECT_PATH is None:
        PROJECT_PATH = str(Path(__file__)).split('CuteAide')[0] + 'CuteAide'
        PROJECT_PATH.replace('\\', '/')
    return PROJECT_PATH

def path_conn(file_name: str='') -> str:
    return project_path() + file_name

if __name__ == '__main__':
    print(project_path())