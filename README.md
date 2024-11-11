# Object Detection Web Application
This project is a web-based object detection application built with Flask and YOLOv5. Users can upload images, view them in a gallery, and analyze them to detect, count various objects and the most common objects detected across all uploaded images.

# Features
* Image Upload: Upload multiple images for object detection.
* Image Gallery: View uploaded images in a gallery format.
* Object Detection: Analyze uploaded images to detect and count objects using the YOLOv5 model.
* Display Results: See object detection results with counts for each detected class, including the most common object.

# Technologies Used
* Flask: For the web framework and handling routes.
* YOLOv5 (Ultralytics): For object detection in images.
* PIL (Pillow): To handle image processing.
* HTML and Jinja2: For creating the frontend templates.

# Installation
1. Clone the repository:
```sh
git clone https://github.com/HaykuhiGhalamdaryan/Projects.git
cd ObjectDetection
cd ObjectDetection
```
2. Install dependencies:
```sh
pip install -r requirements.txt
```

# Usage
1. Run the application:
```sh
python app.py
```
2. Navigate to the home page: Open a browser and go to http://127.0.0.1:5000/.
3. Upload Images:
   * Use the file upload form to select and upload images.
   * Uploaded images will be displayed in the gallery.
4. Analyze Images:
   * Click "Analyze" to detect objects in uploaded images.
   * Detected objects will be counted and displayed, along with the most common object.

# Project Structure
* app.py: Main Flask application file.
* templates/: HTML templates for uploading images, viewing the gallery, and displaying analysis results.
* uploads/: Folder where uploaded images are stored.

# Contributing
Contributions are welcome! If you'd like to add features or fix bugs, feel free to submit a pull request.

# License
This project is licensed under the MIT License.
