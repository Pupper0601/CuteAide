#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

from concurrent.futures import ThreadPoolExecutor

# 创建一个全局的线程池
global_thread_pool = ThreadPoolExecutor(max_workers=15)