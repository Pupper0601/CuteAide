from PIL import Image
from skimage import metrics
from skimage.transform import resize
import numpy as np


# 打开并调整图像大小
image1 = Image.open('5.png')
image2 = Image.open('6.png')
image1 = image1.resize((500, 500))  # 调整图像1的大小为500x500
image2 = image2.resize((500, 500))  # 调整图像2的大小为500x500

# 将图像转换为灰度图像
image1_gray = image1.convert("L")
image2_gray = image2.convert("L")

# 将图像转换为NumPy数组
image1_array = np.array(image1_gray)
image2_array = np.array(image2_gray)

# 计算结构相似性指数（SSIM）
similarity = metrics.structural_similarity(image1_array, image2_array)

# 将相似性指数转换为相似度（范围0到1，值越大表示相似度越高）
similarity = (similarity + 1) / 2
print(similarity)