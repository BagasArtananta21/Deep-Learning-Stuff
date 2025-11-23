from flask import Flask, render_template, request
import os
from utils.detect import run_detection, run_detection_video
from utils.convert import convert_to_jpg

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    uploaded = request.files['image']
    method = request.form.get('method')

    if not uploaded:
        return "No File Uploaded"

    input_path = os.path.join('static/uploads/images', uploaded.filename)
    uploaded.save(input_path)
    input_path = convert_to_jpg(input_path)

    output_path, results = run_detection(input_path, method=method)

    return render_template(
        'result.html',
        input_image=input_path,
        output_image=output_path,
        results=results,
        method=method
    )

@app.route('/detectVideo', methods=['POST'])
def detectVideo():
    uploaded = request.files['video']
    if not uploaded:
        return "No File Uploaded"

    input_path = os.path.join('static/uploads/videos', uploaded.filename)
    uploaded.save(input_path)

    output_path, class_count = run_detection_video(input_path)

    return render_template(
        'resultVideo.html',
        input_video=input_path,
        output_video=output_path,
        counts=class_count
    )

if __name__ == "__main__":
    app.run(debug=True)
