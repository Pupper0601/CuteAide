#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import os
import re

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

from tools.log import logger


def preprocess_image(image):
    # 高斯模糊去噪
    blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
    return blurred_image

def adaptive_binarize_image(image, block_size=5, C=2):
    # 应用自适应二值化
    binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)
    # 保存二值化后的图片
    # cv2.imwrite(save_path, binary_image)
    return binary_image

def pyramid_image(image, levels=3):
    # 构建图像金字塔
    pyramid = [image]
    for i in range(1, levels):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid

def compare_images(source_img, temp_img, win_size=3):
    # 读取图片
    image1 = cv2.imread(source_img, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(temp_img, cv2.IMREAD_GRAYSCALE)

    # 预处理图像
    image1 = preprocess_image(image1)
    image2 = preprocess_image(image2)

    # 应用自适应二值化
    image1 = adaptive_binarize_image(image1)
    image2 = adaptive_binarize_image(image2)

    # 调整图片大小
    image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

    # 构建图像金字
    pyramid1 = pyramid_image(image1)
    pyramid2 = pyramid_image(image2)

    # 计算每一层的 SSIM
    ssim_scores = []
    for img1, img2 in zip(pyramid1, pyramid2):
        img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
        ssim_score, _ = ssim(img1, img2, full=True,win_size=win_size)
        ssim_scores.append(ssim_score)

    # 计算 SSIM
    # ssim_score, _ = ssim(image1, image2, full=True)

    # 计算直方图相似度
    hist1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
    hist1 = cv2.normalize(hist1, hist1).flatten()
    hist2 = cv2.normalize(hist2, hist2).flatten()
    hist_similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    ss = float(round(np.mean(ssim_scores), 2))
    hs = round(hist_similarity, 2)

    if ss >0.5 and hs > 0.9:
        return [source_img.split('\\')[-1][:-4], ss, hs]
    else:
        return None

def current_equipment(source_path, temp_img):
    gun_data = []

    for key, value in source_path.items():
        mod_name = compare_images(value, temp_img)
        if mod_name is not None:
            gun_data.append(mod_name)
    if len(gun_data) == 0:
        gun_data.append([temp_img.split('/')[-1].split('_')[0]+ "_none", 1.0, 1.0])

    gun_nane = ''
    ss = 0
    hs = 0
    for i in gun_data:
        if i[1] >= ss and i[2] >= hs:
            gun_nane = i[0]
            ss = i[1]
            hs = i[2]
    return gun_nane



if __name__ == '__main__':
    # 示例用法
    image_path1 = 'X6.png'
    image_path2 = 'scope_2.png'
    hist_similarity = compare_images(image_path1, image_path2,)
    print(f'图片相似度 (SSIM): {hist_similarity}')
