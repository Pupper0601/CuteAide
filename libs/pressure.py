#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from libs.ghub import GhubDevice


class Pressure:
    def __init__(self):
        self.ghub = GhubDevice()

    def press_key(self, key):
        self.ghub.key_down(key)
        self.ghub.key_up(key)