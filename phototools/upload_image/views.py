#from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import UploadedImage
from django.core.urlresolvers import reverse
from .forms import UploadImageForm
from grayscale.views import ConvertToGray
from grayscale.views import md5hash
from django.conf import settings
import os

# index, presents user with a form to upload an image, uses grayscale.views.ConvertToGray to turn it to b/w
def index(request):
    # if user has submitted a form
    if request.method == 'POST':
        form = UploadImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            mediaDirectory=settings.MEDIA_ROOT
            filename=instance.image.name
            mediaFullPath= os.path.join(mediaDirectory, filename)
            GrayScaleImg=ConvertToGray(mediaFullPath)
            context = {
                "instance" : instance,
                "grayscaleimg" : GrayScaleImg
            }

            return render(request, 'upload_image_templates/list.html', context)
    #if user hasn't submitted anything
    else:
        form = UploadImageForm
        context = {
            "form" : form,
        }
        return render(request, 'upload_image_templates/post_form.html', context)

#class IndexView(TemplateView):
#    model = UploadedImage
#    template_name = 'upload_image_templates/post_form.html'
#    form_class = UploadImageForm
#    success_url = '/grayscale/'
#
#    def form_valid (self, form):
#        form.save(commit = True)
#        return super(IndexView, self).form_valid(form )
