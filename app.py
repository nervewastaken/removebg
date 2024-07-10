from flask import Flask, request, send_file, jsonify, render_template
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)

# Directory to save images without background
OUTPUT_DIR = "output_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove_bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']
    img = Image.open(image_file.stream)

    # Remove background
    img_no_bg = remove(img)

    # Ensure the output path has a .png extension
    output_path = os.path.join(OUTPUT_DIR, os.path.splitext(image_file.filename)[0] + '.png')
    img_no_bg.save(output_path)

    return jsonify({"message": "Background removed successfully", "filename": os.path.basename(output_path)})

@app.route('/get_image/<filename>', methods=['GET'])
def get_image(filename):
    output_path = os.path.join(OUTPUT_DIR, filename)
    if not os.path.exists(output_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
