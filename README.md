# 🚀 YOLOv11 Marine Life Detection & Enhancement System

A robust Computer Vision web application built with **Flask** and **Ultralytics YOLOv11**. This project provides real-time object detection for marine life (seafood), featuring advanced **Image Enhancement** (CLAHE, HE) and **Quantitative Analysis** for evaluating image quality under various lighting conditions.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![YOLOv11](https://img.shields.io/badge/Model-YOLOv11-purple)
![OpenCV](https://img.shields.io/badge/Library-OpenCV-red)

## 🐟 Supported Classes (Custom Model)

This application is powered by a model specifically **fine-tuned** to classify **5 types of marine life**. It demonstrates the practical application of object detection in the fishery/marine sector:

1.  **Udang** (Shrimp)
2.  **Cumi-cumi** (Squid)
3.  **Ikan Tuna** (Tuna Fish)
4.  **Kepiting** (Crab)
5.  **Kerang** (Shellfish/Clam)

---

## ✨ Key Features

### 1. 📷 Smart Image Detection
* **Custom Class Detection:** Uses a custom-trained `best.pt` model to detect the 5 marine classes with high accuracy.
* **Image Enhancement Filters:** Improve detection on low-quality or underwater images using:
    * **CLAHE** (Contrast Limited Adaptive Histogram Equalization) - *Recommended for underwater clarity*
    * **HE** (Histogram Equalization)
    * **Contrast Stretching** (Percentile-based)
    * **Brightness Adjustment**
* **Quantitative Reporting:** Automatically calculates and prints **Brightness (Mean)** and **Contrast (Std Dev)** metrics to the terminal to validate enhancement effectiveness.

### 2. 🎥 Advanced Video Analytics
* **Real-time Tracking:** Implements object tracking to assign unique IDs to marine animals moving in the frame.
* **Unique Counting:** Accurately counts objects (e.g., "**Udang: 5**", "**Kepiting: 2**") based on unique IDs, ensuring moving objects aren't counted multiple times.
* **Visual Counter:** Overlays real-time counts directly onto the video output.
* **Auto-Conversion:** Automatically handles `.avi` to `.mp4` conversion using MoviePy for seamless browser playback.

### 3. 💻 Modern UI/UX
* Responsive interface with tabbed navigation (Image vs Video).
* Clean, gradient-based styling (CSS3).
* Direct download buttons for processed results.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI/ML:** Ultralytics YOLOv11, PyTorch
* **Computer Vision:** OpenCV (`cv2`), NumPy
* **Video Processing:** MoviePy
* **Frontend:** HTML5, CSS3, JavaScript

---

## ⚙️ Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/BagasArtananta21/Deep-Learning-Stuff.git](https://github.com/BagasArtananta21/Deep-Learning-Stuff.git)
    cd Deep-Learning-Stuff
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, install manually: `pip install flask ultralytics opencv-python moviepy numpy`)*

4.  **Prepare the Model**
    * Place your custom trained YOLO model (`best.pt`) inside the `models/` directory.

---

## 🚀 Usage

1.  **Run the Application**
    ```bash
    python app.py
    ```

2.  **Access the Web Interface**
    * Open your browser and go to: `http://127.0.0.1:5000`

3.  **Detecting Images:**
    * Select the **Image Detection** tab.
    * Choose a file (e.g., photo of a crab or tuna).
    * (Optional) Select an Enhancement method (e.g., CLAHE) to improve visibility.
    * Click **Detect**.
    * *Check your terminal to see the Quantitative Analysis report!*

4.  **Detecting Videos:**
    * Select the **Video
