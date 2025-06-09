import cv2
import numpy as np
import os
from glob import glob

# -------- SETUP --------
input_folder = r"D:\projects_github\color_detection\Sample_images"
output_base = "D:\projects_github\color_detection\ouput"

# Define color ranges in HSV
color_ranges = {
    "red":    ([0, 100, 100], [10, 255, 255]),
    "green":  ([36, 100, 100], [86, 255, 255]),
    "blue":   ([94, 80, 2], [126, 255, 255]),
    "yellow": ([20, 100, 100], [30, 255, 255])
}

# -------- CREATE OUTPUT FOLDERS --------
for color in color_ranges.keys():
    os.makedirs(os.path.join(output_base, color), exist_ok=True)

# -------- PROCESS EACH IMAGE --------
image_paths = glob(os.path.join(input_folder, "*.jpg")) + glob(os.path.join(input_folder, "*.png"))

for img_path in image_paths:
    img_name = os.path.basename(img_path)
    image = cv2.imread(img_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    for color, (lower, upper) in color_ranges.items():
        lower_np = np.array(lower)
        upper_np = np.array(upper)

        mask = cv2.inRange(hsv, lower_np, upper_np)
        result = cv2.bitwise_and(image, image, mask=mask)

        output_path = os.path.join(output_base, color, img_name.replace(".", f"_{color}."))
        cv2.imwrite(output_path, result)
        print(f"Saved: {output_path}")
