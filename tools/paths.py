#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from pathlib import Path

def project_path() -> str:
    obj_path = str(Path(__file__)).split('CuteAide')[0]+'CuteAide'
    return obj_path

def path_conn(file_name: str) -> str:
    return project_path() + file_name




if __name__ == '__main__':
    print(project_path())