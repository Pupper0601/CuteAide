import cv2
import numpy as np

def are_images_similar(image1_path, image2_path, similarity_threshold=0.15):
    """
    判断两张图片是否相似

    :param image1_path: 第一张图片的路径
    :param image2_path: 第二张图片的路径
    :param similarity_threshold: 相似度阈值，用于判断两张图片是否相似
    :return: 如果相似则返回True，否则返回False
    """
    # 读取两张彩色图片
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # 检查图片是否读取成功
    if img1 is None or img2 is None:
        raise ValueError("无法读取图片，请检查路径是否正确")

    # 初始化SIFT特征提取器
    sift = cv2.SIFT_create()

    # 检测关键点和描述符
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # 如果没有找到关键点或描述符，则认为图片不相似
    if len(keypoints1) == 0 or len(keypoints2) == 0:
        return False

    # 使用FLANN匹配器进行特征匹配
    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    # 使用Lowe的比率测试来筛选好的匹配点
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # 判断两张图片是否相似
    if len(good_matches) > similarity_threshold * min(len(keypoints1), len(keypoints2)):
        return True
    else:
        return False

# 示例调用
image1_path = '1.png'
image2_path = '2.png'
similarity = are_images_similar(image1_path, image2_path)
print(f"两张图片是否相似: {similarity}")
