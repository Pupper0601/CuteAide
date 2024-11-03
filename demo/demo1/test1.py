import cv2
from skimage.metrics import structural_similarity as ssim

def compare_images_with_ssim(img1_path, img2_path):
    # Read images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Convert images to grayscale
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Resize images to the same size
    img2_gray = cv2.resize(img2_gray, (img1_gray.shape[1], img1_gray.shape[0]))

    # Compute SSIM between the two images
    score, _ = ssim(img1_gray, img2_gray, full=True)
    return score

# Example usage
img1_path = '3.png'
img2_path = '4.png'
similarity_score = compare_images_with_ssim(img1_path, img2_path)
print(f"Similarity score: {similarity_score:.2f}")