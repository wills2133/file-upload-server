# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request, jsonify
from flask import Response
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from datetime import datetime
import os
import shutil
import json
from base64 import decodestring

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = './app/caches'
configure_uploads(app, photos)

@app.route("/")
def index():
    return "Hello Flask"
    # return render_template("index.html")


