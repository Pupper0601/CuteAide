#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


class ReadImage:
    def __init__(self,image_path):
        self.image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        self.binary = None
        self.pyramid = None
        self.adaptive_binarize_image()
        self.pyramid_image()

    def preprocess_image(self):
        # 高斯模糊去噪
        blurred_image = cv2.GaussianBlur(self.image, (3, 3), 0)
        return blurred_image

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
        self.source_img = ReadImage(source_img)
        self.temp_img = ReadImage(temp_img)
        self.source_name = source_name
        self.contrast = self.img_list

    def img_list(self):
        ss = self._ssim()
        hs = self._calc_hist()
        if ss > 0.5 and hs > 0.9:
            return [self.source_name, ss, hs]

    def _ssim(self):
        ssim_scores = []
        for img1, img2 in zip(self.source_img.pyramid, self.temp_img.pyramid):
            img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
            ssim_score, _ = ssim(img1, img2, full=True,win_size=3)
            ssim_scores.append(ssim_score)
        return float(round(np.mean(ssim_scores), 2))

    def _calc_hist(self):
        hist1 = cv2.calcHist([self.source_img.binary], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([self.temp_img.binary], [0], None, [256], [0, 256])
        cv2.normalize(hist1, hist1, 0, 1, cv2.NORM_MINMAX)
        cv2.normalize(hist2, hist2, 0, 1, cv2.NORM_MINMAX)
        _hist = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
        return round(_hist, 2)


if __name__ == '__main__':
    source_img = '2.png'
    temp_img = '6-1.png'
    contrast = ContrastImage('source',source_img, temp_img)
    print(contrast.contrast())



