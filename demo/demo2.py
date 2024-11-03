import os
import cv2
import numpy as np
import pyautogui
from skimage.metrics import structural_similarity as ssim

def take_screenshots(regions, save_paths):
    for region, save_path in zip(regions, save_paths):
        img = pyautogui.screenshot(region=region)
        img.save(save_path)

def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Convert images to grayscale
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Resize images to the same size
    img2_gray = cv2.resize(img2_gray, (img1_gray.shape[1], img1_gray.shape[0]))

    # Compute Structural Similarity Index (SSI)
    score, _ = ssim(img1_gray, img2_gray, full=True)
    return score

def find_similar_images(screenshot_paths, folder_paths, threshold=0.9):
    results = {}
    for screenshot_path, folder_path in zip(screenshot_paths, folder_paths):
        similar_images = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                similarity = compare_images(screenshot_path, file_path)
                if similarity >= threshold:
                    similar_images.append((filename, similarity))
        results[screenshot_path] = similar_images
    return results

# Define screenshot regions and save paths
regions = [
    [1375,98,50,12],
    [1609, 123, 42, 15],
    [1338, 242, 40, 40],
    [1440, 242, 40, 40],
    [1762, 242, 40, 40],
    [1375,324,50,12],
    [1609, 350, 42, 15],
    [1338, 465, 40, 40],
    [1440, 465, 40, 40],
    [1762, 465, 40, 40]
]
screenshot_paths = [
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
    "7.png",
    "8.png",
    "9.png",
    "10.png",
]
folder_paths = [
    "../basic_data/1920_1080/weapons",
    "../basic_data/1920_1080/scopes",
    "../basic_data/1920_1080/muzzles",
    "../basic_data/1920_1080/grips",
    "../basic_data/1920_1080/stocks",
    "../basic_data/1920_1080/weapons",
    "../basic_data/1920_1080/scopes",
    "../basic_data/1920_1080/muzzles",
    "../basic_data/1920_1080/grips",
    "../basic_data/1920_1080/stocks",
]

# Take and save screenshots
take_screenshots(regions, screenshot_paths)

# Find images with similarity greater than 90%
results = find_similar_images(screenshot_paths, folder_paths)
for screenshot_path, similar_images in results.items():
    for filename, similarity in similar_images:
        print(f"{screenshot_path} results: Found similar image: {filename} with similarity: {similarity:.2f}")