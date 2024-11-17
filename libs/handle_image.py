#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import time

# demo3.py
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim



class ReadImage:
    def __init__(self,image):
        """
        读取图片, 并对图片进行预处理
        :param image: 图片路径
        """
        if isinstance(image, str):
            image = cv2.imread(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.image = image
        self.binary = None  # 二值化图像
        self.pyramid = None # 图像金字塔
        self.adaptive_binarize_image()
        self.pyramid_image()

    def preprocess_image(self):
        # 高斯模糊去噪
        blurred_image = cv2.GaussianBlur(self.image, (3, 3), 0)
        return cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

    def adaptive_binarize_image(self,block_size=5, C=2):
        # 应用自适应二值化
        binary_image = cv2.adaptiveThreshold(self.preprocess_image(), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                             block_size,C)
        self.binary = binary_image

    def pyramid_image(self, levels=3):
        # 构建图像金字塔
        if self.binary is not None:
            pyramid = [self.binary]
            for i in range(1, levels):
                image = cv2.pyrDown(self.binary)
                pyramid.append(image)
            self.pyramid = pyramid

# 对比图片相似度
class ContrastImage:
    def __init__(self,source_name, source_img, temp_img):
        """
        :param source_name: 图片名称
        :param source_img: 预处理后的源图
        :param temp_img: 截图
        """
        self.source_img = source_img
        self.temp_img = ReadImage(temp_img)
        self.source_name = source_name
        self.result = self.img_list()   # 对比结果, [name, ssim, hist]

    def img_list(self):
        ss = self._ssim()
        hs = self._calc_hist()
        if ss > 0.5 and hs > 0.9:
            return [self.source_name, ss, hs]
        else:
            return []

    def _ssim(self, win_size=3):
        # 计算 SSIM
        ssim_scores = []
        for img1, img2 in zip(self.source_img[1], self.temp_img.pyramid):
            img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
            ssim_score, _ = ssim(img1, img2, full=True, win_size=win_size)
            ssim_scores.append(ssim_score)
        return float(round(np.mean(ssim_scores), 2))

    def _calc_hist(self):
        # 计算直方图相似度
        hist1 = cv2.calcHist([self.source_img[0]], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([self.temp_img.binary], [0], None, [256], [0, 256])
        cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
        cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)
        _hist = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
        return round(_hist, 2)

# 遍历图片对比
def current_equipment(name,category, temp_image):
    gun_data = []

    # 遍历文件夹下所有图片
    for key, value in category.items():
        mod_name = ContrastImage(key, value, temp_image).result
        if mod_name:
            gun_data.append(mod_name)

    if not gun_data:
        gun_data.append([name + "_none", 1.0, 1.0])

    gun_name, ss, hs = '', 0, 0
    for name, ssim_score, hist_score in gun_data:
        if ssim_score >= ss and hist_score >= hs:
            gun_name, ss, hs = name, ssim_score, hist_score
    return gun_name


if __name__ == '__main__':

    temp_img = ReadImage(r'F:\Object\GitHub\CuteAide\basic\1920_1080\scopes\x6.png')
    t = [temp_img.binary, temp_img.pyramid]
    contrast = ContrastImage('source',t,screenshot)
    print(contrast.result)



