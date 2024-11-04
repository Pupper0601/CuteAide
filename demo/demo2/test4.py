import cv2

# 读取图片
img1 = cv2.imread('5.png')
img2 = cv2.imread('6.png')

# 计算MSE
mse = ((img1 - img2) ** 2).mean()

# 显示MSE结果
print('MSE:', mse)

# 计算SSIM
ssim = cv2.compare_ssim(img1, img2, multichannel=True)

# 显示SSIM结果
print('SSIM:', ssim)