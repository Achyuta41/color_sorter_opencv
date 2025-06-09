# 🎨 Color-Based Image Mask Sorter using OpenCV

This project detects specific colors (**red**, **green**, **yellow**, **blue**) in a batch of images and saves the highlighted regions into separate folders.

---

## 🧠 Features

- ✅ Supports **bulk processing** of `.jpg` and `.png` images
- 🎯 Automatically **isolates regions** of specific colors
- 📁 Organizes outputs into **color-based folders**
- ⚡ Uses OpenCV and NumPy for efficient processing

---

## 📂 Folder Structure

opencv1_color_sorter/
├── input_images/ # Add your original images here
├── output/ # Generated automatically: red/, green/, blue/, yellow/
├── color_mask_batch.py # Main script
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

---

## 🚀 How to Run

### 1. Clone the Repo
   git clone https://github.com/your-username/opencv1_color_sorter.git
   cd opencv1_color_sorter

### 2. Install Requirements
    pip install -r requirements.txt

### 3. Add Input Images
    Place your .jpg or .png images inside the input_images/ folder.

### 4. Run the Script
    python color_mask_batch.py

### 5. View Output
Check the output/ folder — it will contain:

output/
├── red/
├── green/
├── blue/
└── yellow/

---

🙋 Author
-**Achyuta K**
-**Computer Vision** Enthusiast | **AI Explorer**
-📍 India