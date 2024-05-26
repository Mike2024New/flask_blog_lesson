from flask import render_template
from app import app
from app import db
from models import Post


@app.route('/')
def index():
    name = "Ivan"
    return render_template("index.html", n=name)
