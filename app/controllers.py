# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request, jsonify
from flask import Response
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from datetime import datetime
import os
import shutil
import json
import base64

cachesDir = './caches/'
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = cachesDir
configure_uploads(app, photos)

@app.route('/imageocr', methods=['GET', 'POST'])
def image():
    message = {}
    # print(request.json)
    if request.method == 'POST':
        if 'imageFile' in request.json and 'stamp' in request.json:
            stamp = request.json['stamp']
            print('receive package stamp: ' + stamp)
            ### save imageFile
            image_path = cachesDir+stamp+'.png'
            image_file = base64.b64decode(request.json['imageFile'])
            with open(image_path,"wb") as f:
                f.write(image_file)
            # filename = photos.save(image_file, stamp+'.png') ## for jpg/png format
            img_url = photos.url(image_path)
            print('saved ' + image_path)
            message = {'img_url':img_url}
            ### save json
            json_path = cachesDir+stamp+'_gv.json'
            with open(json_path, 'w') as f:
                json.dump(request.json['responses_raw'], f, indent=2)
            print('saved ' + json_path)
            message = {'saved json': stamp+'_gv'}
            ### save json
            json_path = cachesDir+stamp+'_nlp.json'
            with open(json_path, 'w') as f:
                json.dump(request.json['responses'], f, indent=2)
            print('saved ' + json_path)
            message = {'saved json': stamp+'_nlp'}
            ### save json
            json_path = cachesDir+stamp+'_sanit.json'
            with open(json_path, 'w') as f:
                json.dump(request.json['labelByServerSanitized'], f, indent=2)
            print('saved ' + json_path)
            message = {'saved json': stamp+'_sanit'}
        else:
            message = {'img_url':'fail_url'}
        return jsonify(status=200, msg=message)
    if request.method == 'GET':
        return jsonify(status=204, msg=message)
    return jsonify(status=400, msg=message)

@app.route('/label', methods=['GET', 'POST'])
def label():
    message = {}
    # print(request.json)
    if request.method == 'POST':
        if 'labelByUser' in request.json and 'stamp' in request.json:
            stamp = request.json['stamp']
            ### save json
            json_path = cachesDir+stamp+'_labeled.json'
            with open(json_path, 'w') as f:
                json.dump(request.json['labelByUser'], f, indent=2)
            print('saved ' + json_path)
            message = {'saved json': stamp+'_labeled'}
        else:
            message = {'save faild ':name+'.json'}
        return jsonify(status=200, msg=message)
    if request.method == 'GET':
        return jsonify(status=204, msg=message)
    return jsonify(status=400, msg=message)


@app.route('/ocr', methods=['GET', 'POST'])
def ocr():
    # url = 'https://vision.googleapis.com/v1/images:annotate?key=' + 'AIzaSyA2MUwd_DK7b9xsAeOY1HkO5ip8XrrWmhE'
    # payload = json.dump(request.json)
    # r = requests.post(url, json = request.json)
    # print (request.json['responses'])
    # print(request.json.keys())
    # if request.method == 'POST' and 'responses' in request.json:
    #     request.json['responses_raw'] = request.json['responses']
    return Response(response=json.dumps(request.json), status=200, mimetype='application/json')
    # return jsonify(status=200, msg=request.json)

@app.route('/imageurls', methods=['GET'])
def imageurls():
    json_file_path = './caches/wills1553837711918orig.json'
    with open(json_file_path, 'r') as f:
        json_imageurls = json.load(f)
    keyWord = request.args.getlist('keyWord')[0]
    cesKey = 'AIzaSyDEZwOzRv8P1ck-wSjlbExEIJwsImLtHRk'
    url = 'https://www.googleapis.com/customsearch/v1?q={}&cx=001848459722732377703%3Abqrqfxulxua&searchType=image&key={}'.format(keyWord, cesKey)
    r = requests.get(url)
    print(keyWord)
    return Response(response=r.content, status=200, mimetype='application/json')



