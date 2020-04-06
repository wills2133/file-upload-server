# file-upload-server
a file upload server, save jpg and json

### for development
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd app
python ../manage.py runserver
```
### for production debug
```
cd app
python main.py
```
### for production
```
docker pull tiangolo/uwsgi-nginx-flask
sudo docker build -t file-uploader .
sudo docker run -d -p  80:80 --name fu file-uploader
```