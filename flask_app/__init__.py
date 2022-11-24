from flask import Flask

app = Flask(__name__)
app.config['SECRET KEY'] = 'boston-house-pricing'

from flask_app import routes