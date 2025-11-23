import cv2
import numpy as np

def apply_brightness(image, value=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

def apply_he(image):
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

def apply_clahe(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)

    limg = cv2.merge((cl, a, b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

def apply_cs(image):
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    y = img_yuv[:,:,0] 
    p_min, p_max = np.percentile(y, (2, 98))

    if p_max == p_min:
        return image 

    stretched = (y.astype('float32') - p_min) * (255.0 / (p_max - p_min))
    stretched = np.clip(stretched, 0, 255).astype('uint8')

    img_yuv[:,:,0] = stretched
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

def calculate_metrics(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean_val = np.mean(gray) 
    std_val = np.std(gray)   
    
    return round(mean_val, 2), round(std_val, 2)