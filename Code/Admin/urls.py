from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.login , name = "Login"),
]