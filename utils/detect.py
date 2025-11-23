from ultralytics import YOLO
import os
import uuid
import cv2
from moviepy import VideoFileClip
from utils.count import video_class_count
from utils.enchance import apply_brightness, apply_clahe, apply_cs, apply_he, calculate_metrics

model = YOLO("models/best.pt")
CLASS_NAMES = model.model.names

def run_detection(image_path, method="original"):
    original_img = cv2.imread(image_path)
    orig_bright, orig_cont = calculate_metrics(original_img)
    processed_img = original_img.copy()

    if method == "he":
        processed_img = apply_he(original_img)
    elif method == "clahe":
        processed_img = apply_clahe(original_img)
    elif method == "brightness":
        processed_img = apply_brightness(original_img)
    elif method == "cs":
        processed_img = apply_cs(original_img)

    new_bright, new_cont = calculate_metrics(processed_img)
    print(f"ENHANCEMENT DATA: {method.upper()}")

    diff_bright = new_bright - orig_bright
    diff_cont = new_cont - orig_cont

    print(f"[Brightness] Awal: {orig_bright:.2f} -> Akhir: {new_bright:.2f} | Bedanya: {diff_bright:+.2f}")
    print(f"[Contrast  ] Awal: {orig_cont:.2f}   -> Akhir: {new_cont:.2f}   | Bedanya: {diff_cont:+.2f}")

    filename = f"{uuid.uuid4()}.jpg"
    save_path = os.path.join("static/results/images", filename)

    results = model.predict(
        source=processed_img,  
        save=True,
        project="static/results/tmp",
        name="",
        exist_ok=True
    )

    r = results[0]
    save_dir = r.save_dir
    yolo_output_file = os.path.join(save_dir, "image0.jpg") 
    
    if os.path.exists(yolo_output_file):
        os.rename(yolo_output_file, save_path)
    else:
        print("Warning: YOLO output file not found")
        cv2.imwrite(save_path, r.plot())

    class_count = {}
    for box in r.boxes:
        cls_id = int(box.cls[0])
        label = CLASS_NAMES.get(cls_id, str(cls_id))
        class_count[label] = class_count.get(label, 0) + 1

    return save_path, class_count

def run_detection_video(video_path):
    temp_extension = ".avi"
    filename = f"{uuid.uuid4()}{temp_extension}"
    avi_output_path = os.path.join("static/results/videos", filename)
    
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
    out = cv2.VideoWriter(avi_output_path, fourcc, fps, (width, height))

    final_summary_count = {} 

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break 

        results = model.predict(frame, conf=0.25, verbose=False)

        res = results[0]

        current_frame_count = video_class_count(res, CLASS_NAMES)

        final_summary_count = current_frame_count 

        annotated_frame = res.plot() 

        text_list = []
        for label, count in current_frame_count.items():
            text_list.append(f"{label}: {count}")
        
        display_text = " | ".join(text_list)

        if display_text:
            cv2.rectangle(annotated_frame, (10, 10), (30 + len(display_text) * 18, 60), (0, 0, 255), -1)

            cv2.putText(annotated_frame, display_text, (20, 45), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

        out.write(annotated_frame)

    cap.release()
    out.release()

    mp4_output_path = avi_output_path.replace(".avi", ".mp4")
    
    try:
        clip = VideoFileClip(avi_output_path)
        clip.write_videofile(mp4_output_path, codec="libx264", audio_codec="aac")

        clip.close() 
    except Exception as e:
        print(f"Error converting video: {e}")

    if os.path.exists(avi_output_path):
        os.remove(avi_output_path)

    return mp4_output_path, final_summary_count