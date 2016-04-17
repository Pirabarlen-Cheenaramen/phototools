from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
import hashlib
import imghdr
from PIL import Image

# index, just a basic template  forwarder
def index(request):
    return render(request, 'grayscale_templates/home.html')

# ConvertToGrat, given an image file's full path, it converts the image to grayscale
def ConvertToGray(imagefile):
    if imghdr.what(imagefile):
        img = Image.open(imagefile).convert('LA')
        img.save(imagefile)
        return True
    return False

# md5hash, given an image file with full path, it calculates the md5 hash of that file
def md5hash(imagefile):
    if imghdr.what(imagefile):
        hasher= hashlib.md5()
        with open(imagefile, 'rb') as anImgFile:
            buf = anImgFile.read()
            hasher.update(buf)
            return (hasher.hexdigest())
    return None

# With template view.
#class IndexView(TemplateView):
#    #model = UploadedImage
#    template_name = 'grayscale_templates/home.html'
