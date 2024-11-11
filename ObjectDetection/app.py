from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from ultralytics import YOLO
from collections import Counter
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = YOLO("yolov5s.pt")

def analyze_images(image_paths):
    all_class_names = []

    for img_path in image_paths:
        img = Image.open(img_path)
        results = model(img)
        class_names = [model.names[int(i)] for i in results[0].boxes.cls]
        all_class_names.extend(class_names)  

    class_counts = Counter(all_class_names)
    return class_counts

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        files = request.files.getlist('files')

        if not files:
            return 'No files uploaded.'

        for file in files:
            if file and file.filename:
                file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        
        return redirect(url_for('gallery'))

    return render_template('upload.html')

@app.route('/gallery')
def gallery():
    image_names = os.listdir(UPLOAD_FOLDER)
    return render_template('gallery.html', images=image_names)

@app.route('/uploads/<filename>')
def send_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/analyze', methods=['POST'])
def analyze():
    image_folder = UPLOAD_FOLDER
    image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
    
    class_counts = analyze_images(image_paths)
    
    all_class_counts = class_counts.items()
    
    most_common_class = class_counts.most_common(1)[0] if class_counts else None
    
    return render_template('gallery.html', images=os.listdir(UPLOAD_FOLDER), all_class_counts=all_class_counts, most_common_class=most_common_class)

if __name__ == '__main__':
    app.run(debug=True)
