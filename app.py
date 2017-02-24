from flask import Flask, render_template, request, url_for, redirect
import flask, itsdangerous
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stats/<token>")
def stats(token):
    return render_template("main.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
