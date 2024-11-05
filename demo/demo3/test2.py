#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def preprocess_image(image):
    # 高斯模糊去噪
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

def adaptive_binarize_image(image, save_path, block_size=5, C=2):
    # 应用自适应二值化
    binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)
    # 保存二值化后的图片
    cv2.imwrite(save_path, binary_image)
    return binary_image

def pyramid_image(image, levels=3):
    # 构建图像金字塔
    pyramid = [image]
    for i in range(1, levels):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid

def compare_images(image_path1, image_path2, save_path1, save_path2, win_size=3):
    # 读取图片
    image1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # 预处理图像
    image1 = preprocess_image(image1)
    image2 = preprocess_image(image2)

    # 应用自适应二值化并保存
    image1 = adaptive_binarize_image(image1, save_path1)
    image2 = adaptive_binarize_image(image2, save_path2)

    # 构建图像金字
    pyramid1 = pyramid_image(image1)
    pyramid2 = pyramid_image(image2)

    # 计算每一层的 SSIM
    ssim_scores = []
    for img1, img2 in zip(pyramid1, pyramid2):
        img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
        ssim_score, _ = ssim(img1, img2, full=True, win_size=win_size)
        ssim_scores.append(ssim_score)

    # 返回平均 SSIM
    return np.mean(ssim_scores)

# 示例用法
image_path1 = 'muzzle_1.png'
image_path2 = 'muzzle_2.png'
save_path1 = 'binary_muzzle_1.png'
save_path2 = 'binary_muzzle_2.png'
ssim_score = compare_images(image_path1, image_path2, save_path1, save_path2)
print(f'图片结构相似度 (SSIM): {ssim_score}')
