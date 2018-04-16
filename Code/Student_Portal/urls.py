from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.login , name = "Login"),
    url(r'^(?P<student_id>[0-9]+)/$', views.profile , name = "profile"),
    url(r'^(?P<student_id>[0-9]+)/Attendance$', views.attendance , name = "attendance"),
    url(r'^(?P<student_id>[0-9]+)/Results$', views.results , name = "results")
]