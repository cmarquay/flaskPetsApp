from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap

import os
import app.inference as inference

app = Flask(__name__)
Bootstrap(app)


"""
Routes
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            image_path = os.path.join("app/static", uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = inference.get_prediction(image_path)
            result = {
                "class_name": class_name,
                "image_path": image_path[4:]
            }
            return render_template("show.html", result=result)
    return render_template("index.html")
