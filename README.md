# 🧬 Blood Cancer Prediction

A Flask web application that predicts the likelihood of blood cancer from key blood-test parameters using a trained machine learning model. Users can enter values manually or upload a lab report in PDF format.

## 🌐 Live Demo

👉 **[Open the app on Render](YOUR_RENDER_LINK_HERE)**

> Note: the app is hosted on Render's free tier, so the first load may take 30–60 seconds while the server wakes up.

## ✨ Features

- Predict blood cancer risk from 5 clinical parameters
- Clean, responsive web interface
- Reference (normal) ranges shown under every input field
- PDF upload option to extract values from a lab report
- Pre-trained model loaded from `blood_cancer_model.pkl`
- Deployed on Render

## 🧪 Input Parameters

| Parameter | Normal Range |
|-----------|--------------|
| RBC count | 4.2 – 6.1 ×10¹²/L |
| Haemoglobin | 12 – 17.5 g/dL |
| Platelet count | 150,000 – 450,000 /µL |
| ECG / Heart rate | 60 – 100 bpm |
| LDH | 140 – 280 U/L |

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn, pandas, NumPy
- **Model storage:** Pickle (`.pkl`)
- **Frontend:** HTML, CSS (Jinja2 templates)
- **Deployment:** Render, Gunicorn

## 📁 Project Structure

```
blood-cancer-prediction/
├── static/                    # CSS, images, JS
├── templates/                 # HTML templates
├── uploads/                   # Uploaded PDF reports
├── app.py                     # Main Flask application
├── blood_cancer_model.pkl     # Trained ML model
├── model.ipynb                # Model training notebook
├── requirements.txt           # Python dependencies
├── .python-version            # Python version for Render
└── README.md
```

## 🚀 Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ashika3526/blood-cancer-prediction.git
   cd blood-cancer-prediction
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the app**
   ```bash
   python app.py
   ```

5. Open **http://127.0.0.1:5000** in your browser.

## ☁️ Deploying on Render

1. Push the project to GitHub.
2. On [Render](https://render.com), create a new **Web Service** and connect the repository.
3. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Make sure `gunicorn` is listed in `requirements.txt`.
5. Click **Deploy**.

## 📖 How to Use

1. Open the app.
2. Enter your RBC count, Haemoglobin, Platelet count, ECG / Heart rate and LDH values.
3. Click **Predict** to see the result.
4. Or click **Continue to PDF Upload** to upload a lab report instead.

## 🧠 Model Details

- Training and evaluation are in `model.ipynb`.
- Algorithm: *(add the algorithm you used, e.g. Random Forest / Logistic Regression)*
- Dataset: *(add dataset name or source)*
- Accuracy: *(add your accuracy score)*

## ⚠️ Disclaimer

This project is for **educational and demonstration purposes only**. It is **not** a medical device and must not be used for diagnosis or treatment decisions. Always consult a qualified doctor or healthcare professional for medical advice.

## 🔮 Future Improvements

- Improve accuracy with a larger, more diverse dataset
- Add more blood parameters (WBC count, blast cells, etc.)
- Better PDF parsing for different lab report formats
- Downloadable prediction report

## 👩‍💻 Author

**Ashika** — [GitHub](https://github.com/Ashika3526)

## 📄 License

This project is licensed under the MIT License.
