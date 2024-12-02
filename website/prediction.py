from flask import Blueprint, render_template, request, send_from_directory
from .app_functions import ValuePredictor, pred
import os
from werkzeug.utils import secure_filename
import json

# Initialize Blueprint for prediction routes
prediction = Blueprint('prediction', __name__)

# Set folder paths
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

# Get the current directory path
dir_path = os.path.dirname(os.path.realpath(__file__))

# Function to load and return doctors for a predicted disease
def get_doctors_for_disease(disease):
    try:
        # Load doctor data from the JSON file
        with open(os.path.join(dir_path, 'doctors.json')) as f:
            doctors_data = json.load(f)
        # Return the doctors for the predicted disease
        return doctors_data.get(disease, [])
    except Exception as e:
        print(f"Error loading doctors data: {e}")
        return []

# Route for handling manual form input predictions
@prediction.route('/predict', methods=["POST", 'GET'])
def predict():
    if request.method == "POST":
        # Get form data and convert to a list of floats
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))

        # Use ValuePredictor to get the prediction result and predicted disease
        result, disease = ValuePredictor(to_predict_list) 

        # Fetch relevant doctors based on the predicted disease
        doctors = get_doctors_for_disease(disease)

        # Render the result template with prediction and doctor information
        return render_template("result.html", prediction=result, page=disease, doctors=doctors)
    else:
        return render_template('base.html')

# Route for handling image file uploads and deep learning-based predictions (e.g., Pneumonia detection)
@prediction.route('/upload', methods=['POST','GET'])
def upload_file():
    if request.method == "GET":
        return render_template('pneumonia.html', title='Pneumonia Disease')
    else:
        # Handle file upload
        file = request.files["file"]
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
        file.save(file_path)

        # Indices to label the prediction
        indices = {0: 'Normal', 1: 'Pneumonia'}

        # Get the prediction result using a deep learning model
        result = pred(file_path)

        if result > 0.5:
            label = indices[1]
            accuracy = result * 100

            # Fetch relevant doctors for Pneumonia
            doctors = get_doctors_for_disease('Pneumonia')
        else:
            label = indices[0]
            accuracy = 100 - result
            doctors = []  # No doctors needed for a normal result

        # Render the deep_pred template with prediction, accuracy, and doctor information
        return render_template('deep_pred.html', image_file_name=file.filename, label=label, accuracy=accuracy, doctors=doctors)

# Route to send uploaded files back to the user (for displaying the uploaded image)
@prediction.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# from flask import Blueprint, render_template, request, send_from_directory, make_response
# from .app_functions import ValuePredictor, pred
# import os
# from werkzeug.utils import secure_filename
# import json
# import pdfkit

# # Initialize Blueprint for prediction routes
# prediction = Blueprint('prediction', __name__)

# # Set folder paths
# UPLOAD_FOLDER = 'uploads'
# STATIC_FOLDER = 'static'

# # Get the current directory path
# dir_path = os.path.dirname(os.path.realpath(__file__))

# # Configure pdfkit (adjust the path to wkhtmltopdf depending on your environment)
# PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")  # Linux/Mac
# # For Windows, use: PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

# # Function to load and return doctors for a predicted disease
# def get_doctors_for_disease(disease):
#     try:
#         # Load doctor data from the JSON file
#         with open(os.path.join(dir_path, 'doctors.json')) as f:
#             doctors_data = json.load(f)
#         # Return the doctors for the predicted disease
#         return doctors_data.get(disease, [])
#     except Exception as e:
#         print(f"Error loading doctors data: {e}")
#         return []

# # Route for handling manual form input predictions
# @prediction.route('/predict', methods=["POST", 'GET'])
# def predict():
#     if request.method == "POST":
#         # Get form data and convert to a list of floats
#         to_predict_list = request.form.to_dict()
#         to_predict_list = list(to_predict_list.values())
#         to_predict_list = list(map(float, to_predict_list))

#         # Use ValuePredictor to get the prediction result and predicted disease
#         result, disease = ValuePredictor(to_predict_list) 

#         # Fetch relevant doctors based on the predicted disease
#         doctors = get_doctors_for_disease(disease)

#         # Generate HTML to render result
#         rendered_html = render_template("result.html", prediction=result, page=disease, doctors=doctors)
        
#         # Check if user wants to download the result as a PDF
#         if request.form.get('generate_pdf') == 'yes':
#             # Generate the PDF from the HTML
#             pdf = pdfkit.from_string(rendered_html, False, configuration=PDFKIT_CONFIG)

#             # Send the generated PDF to the user for download
#             response = make_response(pdf)
#             response.headers['Content-Type'] = 'application/pdf'
#             response.headers['Content-Disposition'] = 'attachment; filename=prediction_report.pdf'
#             return response

#         # Render the result page
#         return render_template("result.html", prediction=result, page=disease, doctors=doctors)
#     else:
#         return render_template('base.html')

# # Route for handling image file uploads and deep learning-based predictions (e.g., Pneumonia detection)
# @prediction.route('/upload', methods=['POST','GET'])
# def upload_file():
#     if request.method == "GET":
#         return render_template('pneumonia.html', title='Pneumonia Disease')
#     else:
#         # Handle file upload
#         file = request.files["file"]
#         basepath = os.path.dirname(__file__)
#         file_path = os.path.join(basepath, 'uploads', secure_filename(file.filename))
#         file.save(file_path)

#         # Indices to label the prediction
#         indices = {0: 'Normal', 1: 'Pneumonia'}

#         # Get the prediction result using a deep learning model
#         result = pred(file_path)

#         if result > 0.5:
#             label = indices[1]
#             accuracy = result * 100

#             # Fetch relevant doctors for Pneumonia
#             doctors = get_doctors_for_disease('Pneumonia')
#         else:
#             label = indices[0]
#             accuracy = 100 - result
#             doctors = []  # No doctors needed for a normal result

#         # Render the deep_pred template with prediction, accuracy, and doctor information
#         return render_template('deep_pred.html', image_file_name=file.filename, label=label, accuracy=accuracy, doctors=doctors)

# # Route to send uploaded files back to the user (for displaying the uploaded image)
# @prediction.route('/uploads/<filename>')
# def send_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

