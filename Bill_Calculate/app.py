from flask import Flask, render_template, request, jsonify, send_from_directory
from PIL import Image, ImageOps, ImageEnhance
import pytesseract
import re
import os
import json

# Define the base directory for your project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# Set the paths for uploads and processed folders
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'uploads')
app.config['PROCESSED_FOLDER'] = os.path.join(BASE_DIR, 'processed')
app.config['PARAMETERS_FILE'] = os.path.join(BASE_DIR, 'saved_parameters.json')

# Set path to Tesseract executable if necessary (update for your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

current_image = None
items_list = []

# Ensure upload and processed folders exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['PROCESSED_FOLDER']):
    os.makedirs(app.config['PROCESSED_FOLDER'])

def process_image(image_path, contrast, threshold, resize_factor):
    """Process the image based on the user-adjusted parameters."""
    try:
        image = Image.open(image_path)

        # Convert to grayscale
        grayscale_image = ImageOps.grayscale(image)

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(grayscale_image)
        enhanced_image = enhancer.enhance(contrast)

        # Apply thresholding to create a binary image (black and white)
        threshold_image = enhanced_image.point(lambda x: 0 if x < threshold else 255, '1')

        # Resize the image
        width, height = threshold_image.size
        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)
        resized_image = threshold_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        return resized_image

    except Exception as e:
        print(f"Error processing image: {e}")
        raise e

def extract_items_and_prices(receipt_text):
    """Extract food items and their prices from receipt text."""
    lines = receipt_text.split('\n')
    items = []
    subtotal = 0

    for line in lines:
        if re.match(r'-+', line) or not line.strip():
            continue

        match = re.search(r'(.*?)(\d+\.\d{2})$', line)
        if match:
            item = match.group(1).strip()
            price = float(match.group(2).strip())
            items.append({'item': item, 'price': price})
            subtotal += price

    return items, subtotal

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        global current_image
        current_image = filepath

        return jsonify({'message': 'File uploaded successfully', 'filename': file.filename})

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    contrast = data.get('contrast', 2.0)
    threshold = data.get('threshold', 140)
    resize_factor = data.get('resize_factor', 1.5)

    try:
        # Check if an image is available to process
        if current_image is None:
            return jsonify({'error': 'No image uploaded yet to process'})

        processed_image = process_image(current_image, contrast, threshold, resize_factor)

        # Save the processed image
        processed_image_path = os.path.join(app.config['PROCESSED_FOLDER'], 'processed_image.png')
        processed_image.save(processed_image_path)

        # Perform OCR
        receipt_text = pytesseract.image_to_string(processed_image)

        # Extract items
        items, subtotal = extract_items_and_prices(receipt_text)
        global items_list
        items_list = items

        return jsonify({'items': items, 'subtotal': subtotal, 'processed_image_url': f'/processed/processed_image.png?{os.path.getmtime(processed_image_path)}'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/processed/<filename>')
def send_processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.json
    item_name = data.get('item_name')
    item_price = data.get('item_price')

    try:
        if item_name and item_price:
            new_item = {'item': item_name, 'price': float(item_price)}
            items_list.append(new_item)
            return jsonify({'message': 'Item added successfully', 'items': items_list})
        else:
            return jsonify({'error': 'Invalid item name or price'})
    except ValueError:
        return jsonify({'error': 'Invalid item price'})

@app.route('/calculate_split', methods=['POST'])
def calculate_split():
    data = request.json
    discount_percentage = data.get('discount_percentage', 0)
    surcharge_amount = data.get('surcharge_amount', 0.0)
    names_for_items = data.get('names_for_items', [])

    try:
        # Validate and set default values for discount and surcharge
        discount_percentage = float(discount_percentage) if discount_percentage is not None else 0.0
        surcharge_amount = float(surcharge_amount) if surcharge_amount is not None else 0.0

        discount_multiplier = (100 - discount_percentage) / 100

        person_expenses = {}
        for idx, item in enumerate(items_list):
            if idx < len(names_for_items):
                names = [name.strip() for name in names_for_items[idx].split(',') if name.strip()]
            else:
                names = []

            if not names:
                continue
            split_cost = item['price'] / len(names)
            for name in names:
                person_expenses[name] = person_expenses.get(name, 0) + split_cost

        subtotal = sum([item['price'] for item in items_list])
        total = (subtotal + surcharge_amount) * discount_multiplier

        result = {
            'individual_expenses': {person: round(expense * discount_multiplier, 2) for person, expense in person_expenses.items()},
            'subtotal': round(subtotal, 2),
            'total': round(total, 2)
        }
        return jsonify(result)
    except ValueError:
        return jsonify({'error': 'Invalid discount or surcharge value. Please enter valid numbers.'})
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'})

@app.route('/save_parameters', methods=['POST'])
def save_parameters():
    data = request.json
    parameter_name = data.get('parameter_name', 'default')
    try:
        parameters = {}
        if os.path.exists(app.config['PARAMETERS_FILE']):
            with open(app.config['PARAMETERS_FILE'], 'r') as f:
                parameters = json.load(f)

        parameters[parameter_name] = {
            'contrast': data.get('contrast', 2.0),
            'threshold': data.get('threshold', 140),
            'resize_factor': data.get('resize_factor', 1.5)
        }

        with open(app.config['PARAMETERS_FILE'], 'w') as f:
            json.dump(parameters, f)

        return jsonify({'message': 'Parameters saved successfully.'})
    except Exception as e:
        return jsonify({'error': 'Failed to save parameters'})

@app.route('/load_parameters', methods=['GET'])
def load_parameters():
    try:
        if os.path.exists(app.config['PARAMETERS_FILE']):
            with open(app.config['PARAMETERS_FILE'], 'r') as f:
                parameters = json.load(f)
            return jsonify(parameters)
        else:
            return jsonify({'error': 'No saved parameters found'})
    except Exception as e:
        return jsonify({'error': 'Failed to load parameters'})

if __name__ == '__main__':
    app.run(debug=True)
