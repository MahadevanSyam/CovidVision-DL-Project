from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from model import predict_disease

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            result = predict_disease(filepath)
            if result == "COVID":
                result = "Normal"
            elif result == "Normal":
                result = "COVID"
            elif result == "Viral Pneumonia":
                result = "Viral Pneumonia"
            else:
                result = "Lung_Opacity"
            return render_template('index.html', filename=filename, result=result)

if __name__ == '__main__':
    app.run(debug=False)
