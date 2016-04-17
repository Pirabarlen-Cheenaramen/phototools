from django.conf.urls import url

from . import views
app_name='grayscale'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='grayscale'),
]
