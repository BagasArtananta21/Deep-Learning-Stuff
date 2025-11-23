def video_class_count(results_frame, class_names):
    frame_count = {}
    
    for box in results_frame.boxes:
        cls_id = int(box.cls[0])
        label = class_names.get(cls_id, f"class_{cls_id}")
        frame_count[label] = frame_count.get(label, 0) + 1

    return frame_count