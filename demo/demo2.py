# import numpy as np
# from PIL import Image
#
#
# #比对识别图
# def get_hash(img):
#     hash_data = ''
#     image = Image.open(img)
#     image = np.array(image.resize((9, 8), Image.LANCZOS).convert('L'), 'f')
#     for i in range(8):
#         for j in range(8):
#             if image[i, j] > image[i, j + 1]:
#                 hash_data += '1'
#             else:
#                 hash_data += '0'
#     hash_data = ''.join(map(lambda x: '%x' % int(hash_data[x: x + 4], 2), range(0, 64, 4)))  # %x：转换无符号十六进制
#     return hash_data
#
# # get汉明距离
# def get_Hamming(hash1, hash2):
#     Hamming = 0
#     for i in range(len(hash1)):
#         if hash1[i] != hash2[i]:
#             Hamming += 1
#     return Hamming
#
# #   比对两张图片
# def compare2pic(equi, demo, threshold):
#     equi_hash = get_hash(equi)
#     demo_hash = get_hash(demo)
#     distance = get_Hamming(equi_hash, demo_hash)
#     if distance <= threshold:
#         return distance
#     return threshold+1
#
# def image_compare(screenshot, source):
#     tmp_dist = compare2pic(screenshot,source,5)
#     if tmp_dist < 5:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     a = "1.png"
#     b = "BeryM762.png"
#     print(image_compare(a,b))
