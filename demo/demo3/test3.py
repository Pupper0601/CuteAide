#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com


gun_data=  [['buchang-b', 0.56, 1.0], ['xiaoyan-b', 0.51, 1.0], ['xiaoyan-j', 0.74, 1.0], ['xiaoyin-b', 0.93, 1.0],
['xiaoyin-c', 0.83, 1.0], ['xiaoyin-j', 0.91, 1.0]]

if len(gun_data) > 0:
    gun_nane = 'nane'
    ss = 0
    hs = 0
    for i in gun_data:
        if i[1] >= ss and i[2] >= hs:
            gun_nane = i[0]
            ss = i[1]
            hs = i[2]
    print(gun_nane)