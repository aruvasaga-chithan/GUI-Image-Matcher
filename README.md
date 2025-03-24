# 🖼️ Image Matching Tool 🔍

## 🎯 Overview
The **Image Matching Tool** is a Python-based GUI application that allows users to search for similar images in a selected folder using **ORB (Oriented FAST and Rotated BRIEF)** feature detection and matching. 🧠💡

## ✨ Features
✅ Select an image as the search target 📸
✅ Choose a folder containing images to compare 📂
✅ Uses ORB feature detection to find the best match 🧐
✅ Displays the search image and matched image in a GUI 🖥️
✅ Provides user-friendly alerts for matches and errors ⚠️✅

## ⚙️ Installation

### 🛠️ Prerequisites
Ensure you have Python installed (Python 3.7 or later recommended). 🐍

### 📦 Required Libraries
Install the required dependencies using pip:
```sh
pip install opencv-python numpy pillow tk
```

## 🚀 Usage
1️⃣ Run the script using the following command:
   ```sh
   python image_matcher.py
   ```
2️⃣ Click on **Select Search Image** to choose an image. 🖼️
3️⃣ Click on **Select Image Folder** to choose a folder containing images. 📁
4️⃣ Click on **Search for Matches** to start the matching process. 🔍
5️⃣ The application will display the closest matching image if found or notify the user if no matches exist. 📢

## 🧠 How It Works
1️⃣ The ORB detector extracts keypoints and descriptors from the selected search image. 🔑
2️⃣ It compares these descriptors with images in the chosen folder using a **brute-force matcher**. 🤖
3️⃣ Images with an average match distance below a threshold (default: 50) are considered a match. 🎯
4️⃣ The matched image is displayed in the GUI. 🖥️

## 🔧 Troubleshooting
❌ **No matches found:** Try using clearer images or increasing the number of ORB features. 🏞️
❌ **Application crashes or freezes:** Ensure valid images are used and check console logs for errors. 🖥️⚠️
❌ **Missing dependencies:** Reinstall missing libraries using:
```sh
pip install -r requirements.txt
```
(if applicable)

## 👤 Author
**Aruvasaga Chithan** ✍️

---
🎉 Enjoy using the **Image Matching Tool**! 🚀🔍

