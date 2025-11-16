from flask import Flask, render_template, request
from ultralytics import YOLO
import os
from utils.detect import run_detection
from utils.convert import convert_to_jpg


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    uploaded = request.files['image']
    if not uploaded:
        return "No File Uploaded"

    input_path = os.path.join('static/uploads/images', uploaded.filename)
    uploaded.save(input_path)
    input_path = convert_to_jpg(input_path)

    output_path, results = run_detection(input_path)

    return render_template('result.html', input_image=input_path, output_image=output_path, results=results)


# def clean_uploads_and_results():
#     folders = ["static/uploads", "static/results"]
#     for folder in folders:
#         if os.path.exists(folder):
#             for file in os.listdir(folder):
#                 filepath = os.path.join(folder, file)
#                 if os.path.isfile(filepath):
#                     os.remove(filepath)

# atexit.register(clean_uploads_and_results)


if __name__ == '__main__':
    app.run(debug=True)