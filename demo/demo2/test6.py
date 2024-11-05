import os

import numpy as np
from PIL import Image


def current_equipment(temp_img, source_path):
    mod_name = 'none'  #当前配枪
    gun1_distance = 11  #武器识别的汉明距离阈值

    source_path = '../../basic/1920_1080/weapons/'  #预先截取的图片路径
    temp_img = '../6.png' #当前武器图片路径

    content = os.listdir(source_path)
    for each in content:
         abs_source_path = source_path+each
         tmp_dist1 = compare2pic(temp_img,abs_source_path,10)
         if tmp_dist1 < gun1_distance:
              mod_name = str(each)[:-4]

    print('1号武器是：'+mod_name)
    return mod_name

#  比对两张图片
def compare2pic(equi, demo, threshold):
    equi_hash = get_hash_value(equi)         #获取图片哈希值
    demo_hash = get_hash_value(demo)         #获取图片哈希值
    distance = get_hamming(equi_hash, demo_hash)
    if distance <= threshold:
         return distance
    return threshold+1


# 获取图片哈希值
def get_hash_value(img):
    hash_data = ''     #哈希值
    image = Image.open(img)  #打开图片
    image = np.array(image.resize((9, 8), Image.LANCZOS).convert('L'), 'f')  #转换图片格式
    for i in range(8):
         for j in range(8):
              if image[i, j] > image[i, j + 1]:
                    hash_data += '1'
              else:
                    hash_data += '0'
    hash_data = ''.join(map(lambda x: '%x' % int(hash_data[x: x + 4], 2), range(0, 64, 4)))  # %x：转换无符号十六进制
    return hash_data

#汉明距离
def get_hamming(hash1, hash2):
    hamming = 0        #汉明距离
    for i in range(len(hash1)):        #计算汉明距离
         if hash1[i] != hash2[i]:      #不同
              hamming += 1          #汉明距离加1
    return hamming         #返回汉明距离

if __name__ == '__main__':
     current_equipment()
