# phototools
Just a sample django 1.9 and python3 project to show django's internal urls,models, views and template at work. This project allows a user to upload a picture and then it converts the image into grayscale before submitting that to the user. NO CLEANUP of those pictures are done. No frontend beautification has been done.


This is not meant for production environment
grayscale is implemented via PIL.image, see grayscale/views.py
uploader is handled in upload_image/views.py

You can now add further image functions to it and  link it via uploader, or make a new app to make an interface.
## Installation
**** `cd phototools`
* `pip3 install -r requirements.txt`
* `cd phototools`
* `python3 manage.py runserver 8080`
* open up your browser and go to http://127.0.0.1:8080

##TODO:
1. add a REST api for image details 2.
2. Remove file on server or store hash of file before processing to prevent duplicate uploads.



