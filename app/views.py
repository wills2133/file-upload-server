# -*- coding: utf-8 -*-
from app import app

@app.route("/")
def index():
    return "Hello Flask"
    # return render_template("index.html")


