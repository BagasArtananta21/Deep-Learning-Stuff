# 🚀 YOLOv8 Web Detection & Enhancement System

A robust Computer Vision web application built with **Flask** and **Ultralytics YOLOv8**. This project provides real-time object detection for images and videos, featuring advanced **Image Enhancement** (CLAHE, HE) and **Quantitative Analysis** for evaluating image quality.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-purple)
![OpenCV](https://img.shields.io/badge/Library-OpenCV-red)

## ✨ Key Features

### 1. 📷 Smart Image Detection
* **Object Detection:** Uses YOLOv8 (`best.pt`) to detect classes with high accuracy.
* **Image Enhancement Filters:** Improve detection on low-quality images using:
    * **CLAHE** (Contrast Limited Adaptive Histogram Equalization) - *Recommended*
    * **HE** (Histogram Equalization)
    * **Contrast Stretching** (Percentile-based)
    * **Brightness Adjustment**
* **Quantitative Reporting:** Automatically calculates and prints **Brightness (Mean)** and **Contrast (Std Dev)** metrics to the terminal to validate enhancement effectiveness.

### 2. 🎥 Advanced Video Analytics
* **Real-time Tracking:** Implements object tracking to assign unique IDs to objects.
* **Unique Counting:** Accurately counts objects (e.g., "Car: 5") based on unique IDs, not just frame occurrences.
* **Visual Counter:** Overlays real-time counts directly onto the video output.
* **Auto-Conversion:** Automatically handles `.avi` to `.mp4` conversion using MoviePy for seamless browser playback.

### 3. 💻 Modern UI/UX
* Responsive interface with tabbed navigation (Image vs Video).
* Clean, gradient-based styling (CSS3).
* Direct download buttons for processed results.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI/ML:** Ultralytics YOLOv8, PyTorch
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
    * Place your trained YOLO model (`best.pt`) inside the `models/` directory.

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
    * Choose a file.
    * (Optional) Select an Enhancement method (e.g., CLAHE) to improve visibility.
    * Click **Detect**.
    * *Check your terminal to see the Quantitative Analysis report!*

4.  **Detecting Videos:**
    * Select the **Video Detection** tab.
    * Upload an MP4/AVI file.
    * Wait for the processing (Detection + Tracking + Conversion).
    * Download the result with the unique counter overlay.

---

## 📊 Quantitative Analysis (Terminal Output)

The system provides a scientific report for every image processed to measure the impact of enhancement filters.

**Example Terminal Output:**
```text
============================================================
   LAPORAN DATA KUANTITATIF (Metode: CLAHE)
============================================================
METRIK          | SEBELUM    | SESUDAH    | SELISIH   
------------------------------------------------------------
Brightness      | 102.45     | 105.10     | +2.65     
Contrast        | 45.10      | 62.30      | +17.20    
------------------------------------------------------------
>> Status: Detail/Kontras MENINGKAT (Objek lebih tegas).
============================================================
