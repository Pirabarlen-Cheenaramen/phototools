from django.conf.urls import url
from . import views

app_name = 'upload_image'
urlpatterns = [
    url(r'^$', views.index, name='uploadindex'),
]

