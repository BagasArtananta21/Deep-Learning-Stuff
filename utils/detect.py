from ultralytics import YOLO
import os
import uuid

model = YOLO("models/best.pt")  

def run_detection(image_path):
    filename = f"{uuid.uuid4()}.jpg"
    save_path = os.path.join("static/results/images", filename)

    images_extensions = [".jpg", ".jpeg", ".png"]
    if not any(image_path.lower().endswith(ext) for ext in images_extensions):
        raise ValueError("Unsupported file format. Please upload an image file.")

    results = model.predict(source=image_path, save=True, project="static/results/tmp", name="", exist_ok=True)

    result_img_path = results[0].save_dir + "/" + os.path.basename(image_path)

    os.rename(result_img_path, save_path)

    class_count = {}
    for box in results[0].boxes:
        cls = int(box.cls[0])
        class_count[cls] = class_count.get(cls, 0) + 1

    return save_path, class_count

