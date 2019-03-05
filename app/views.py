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

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    message = {}
    # print(request.json)

    if request.method == 'POST' and 'image' in request.json:
        name = request.json['name']
        print('receive package name: ' + name)
        ### save image
        image_file = decodestring(request.json['image'])
        image_path = "./app/caches/"+name+'.png'
        with open(image_path,"wb") as f:
            f.write(image_file)
        # filename = photos.save(image_file, name+'.png')
        img_url = photos.url(image_path)
        print('saved image')
        ### save json
        json_path = "./app/caches/"+name+'.json'
        with open(json_path, 'w') as f:
            json.dump(request.json['res'], f)
        print('saved json')
        message = {'img_url':img_url}
    else:
        message = {'img_url':'fail_url'}
    return jsonify(status="success", msg=message)

@app.route("/")
def index():
    return "Hello Flask"
    # return render_template("index.html")


