from flask import render_template, request
from flask_app import app
import pickle
import numpy as np
import logging
from flask.logging import default_handler

prediction_text = ''
lm = pickle.load(open('/Users/notaryanramani/Documents/VSCodePython/BostonHousing/boston-housing-regression/boston_lm.pkl', 'rb'))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('housing-logs.log')
logger.addHandler(file_handler)
logger.removeHandler(default_handler)

@app.route('/')
def home():
    return render_template('home.html', prediction_text=prediction_text)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form.to_dict().values()
        # print(data)
        if '' in data:
            prediction_text = 'NaN'
        else:
            test = [float(x) for x in data]
            result = lm.predict(np.array(test).reshape(1, -1))
            prediction_text = str((float('%.2f' % result[0]) * 1000)) + ' USD'
        logger.info('Input: {} \nOutput: {}'.format(data, prediction_text))
    return render_template('home.html', prediction_text=prediction_text)

@app.route('/about')
def about():
    return render_template('about.html')

