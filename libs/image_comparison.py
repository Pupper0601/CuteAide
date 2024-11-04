#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import os

import PIL
import numpy as np
from PIL import ImageGrab
from PIL import Image


def current_equipment(temp_img, source_path):
    mod_name = 'none'  #当前配枪
    gun1_distance = 6  #武器识别的汉明距离阈值

    content = os.listdir(source_path)
    for each in content:
         abs_source_path = source_path+each
         tmp_dist1 = _compare2pic(temp_img,abs_source_path,10)
         if tmp_dist1 < gun1_distance:
              mod_name = str(each)[:-4]
    return mod_name

#  比对两张图片
def _compare2pic(equi, demo, threshold):
    equi_hash = _get_hash_value(equi)         #获取图片哈希值
    demo_hash = _get_hash_value(demo)         #获取图片哈希值
    distance = _get_hamming(equi_hash, demo_hash)
    if distance <= threshold:
         return distance
    return threshold+1


# 获取图片哈希值
def _get_hash_value(img):
    hash_data = ''     #哈希值
    image = Image.open(img)  #打开图片
    image = np.array(image.resize((9, 8), PIL.Image.Resampling.LANCZOS).convert('L'), 'f')  #转换图片格式
    for i in range(8):
         for j in range(8):
              if image[i, j] > image[i, j + 1]:
                    hash_data += '1'
              else:
                    hash_data += '0'
    hash_data = ''.join(map(lambda x: '%x' % int(hash_data[x: x + 4], 2), range(0, 64, 4)))  # %x：转换无符号十六进制
    return hash_data

#汉明距离
def _get_hamming(hash1, hash2):
    hamming = 0        #汉明距离
    for i in range(len(hash1)):        #计算汉明距离
         if hash1[i] != hash2[i]:      #不同
              hamming += 1          #汉明距离加1
    return hamming         #返回汉明距离

if __name__ == '__main__':
     current_equipment()
