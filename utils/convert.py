from PIL import Image
import os

def convert_to_jpg(input_path):
    img = Image.open(input_path)

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    output_path = os.path.splitext(input_path)[0] + ".jpg"
    
    img.save(output_path, "JPEG", quality=95)

    if input_path.lower() != output_path.lower():
        os.remove(input_path)

    return output_path
