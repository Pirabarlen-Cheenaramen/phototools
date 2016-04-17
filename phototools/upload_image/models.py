from django.core.urlresolvers import reverse
from django.db import models
#selven resume here
# Create your models here.
class UploadedImage(models.Model):
    image = models.FileField(null = True, blank = True )
