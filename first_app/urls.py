from django.urls import re_path as url
from first_app import views


urlpatterns = [
    url(r'^$', views.first, name='index'),
    
]