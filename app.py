from flask import Flask, render_template, request
from ultralytics import YOLO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)