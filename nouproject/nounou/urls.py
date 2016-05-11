from django.conf.urls import patterns, url
from django.contrib import admin
from nounou import views
from .views import *





urlpatterns = [
    url(r'^', landing, name='landing'),
]

