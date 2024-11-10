#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def showImage(name, img):
    plt.imshow(img, cmap="gray")
    plt.title(name)
    plt.show()


def AdaptiveThreshold(img):
    C = 6
    win = 5
    img_blur = cv.blur(img, (win, win))
    img2 = np.uint8(img > img_blur - C) * 255
    print(img2)
    return img2


def AdaptiveThreshold2(img):
    alpha = 0.05
    win = 5
    img_blur = cv.GaussianBlur(img, (win, win), 5)
    img2 = np.uint8(img > (1 - alpha) * img_blur) * 255
    return img2


if __name__ == "__main__":
    img = cv.imread("2.png", 0)
    img2 = AdaptiveThreshold(img)
    img3 = AdaptiveThreshold2(img)
    showImage("img", img)
    showImage("img2", img2)
    showImage("img3", img3)