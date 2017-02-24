from flask import Flask, render_template, request, url_for, redirect
import flask
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")




if __name__ == '__main__':
    app.debug = True
    app.run()
