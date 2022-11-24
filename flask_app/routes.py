from flask import render_template
from flask_app import app



@app.route('/')
def home():
    return render_template('home.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
        return render_template('home.html', prediction_text='AFTER SUBMIT')
