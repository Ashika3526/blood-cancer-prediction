from flask import Flask, render_template, request
import joblib, os
import pandas as pd
from astropy.io import fits# PyMuPDF

app = Flask(__name__)

# Load the model
model = joblib.load('blood_cancer_model.pkl')

# Upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ----------------------------------------
# PDF Extraction Function
# ----------------------------------------
def extract_values_from_pdf(file_path):
    text = ''
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()

    def find_val(key):
        for line in text.splitlines():
            if key.lower() in line.lower():
                parts = line.split(':')
                if len(parts) > 1:
                    try:
                        return float(parts[1].strip().split()[0])
                    except:
                        return None
        return None

    return {
        'RBC count': find_val('RBC'),
        'Haemoglobin': find_val('Haemoglobin'),
        'Platelet count': find_val('Platelet'),
        'ECG / Heart rate': find_val('Heart rate'),
        'LDH': find_val('LDH')
    }

# ----------------------------------------
# Routes
# ----------------------------------------

# Page 1: Manual Entry
@app.route('/')
def home():
    return render_template('index.html', result=None)

# Prediction from Manual Entry
@app.route('/predict', methods=['POST'])
def predict():
    try:
        rbc = float(request.form['rbc'])
        haemoglobin = float(request.form['haemoglobin'])
        platelet = float(request.form['platelet'])
        ecg = float(request.form['ecg'])
        ldh = float(request.form['ldh'])

        input_data = pd.DataFrame([[rbc, haemoglobin, platelet, ecg, ldh]],
            columns=['RBC count', 'Haemoglobin', 'Platelet count', 'ECG / Heart rate', 'LDH'])

        prediction = model.predict(input_data)[0]
        return render_template('index.html', result=prediction)
    
    except Exception as e:
        return render_template('index.html', error=str(e))

# Page 2: PDF Upload Page
@app.route('/upload_page')
def show_upload_page():
    return render_template('upload.html', result=None)

# PDF Upload Prediction
@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['pdf']
        if file and file.filename.endswith('.pdf'):
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)

            values = extract_values_from_pdf(path)

            if None in values.values():
                return render_template('upload.html', error="Could not extract all values from PDF.")

            df = pd.DataFrame([list(values.values())], columns=list(values.keys()))
            prediction = model.predict(df)[0]
            return render_template('upload.html', result=prediction)

        return render_template('upload.html', error="Invalid file. Please upload a PDF.")
    
    except Exception as e:
        return render_template('upload.html', error=str(e))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
