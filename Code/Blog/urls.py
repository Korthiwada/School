from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path

app_name="Blog"

urlpatterns = [
    url(r'^$', views.index , name="index"),
    url(r'^career/$', views.career , name="career"),
    url(r'^admissions/$', views.admission , name="admission"),
    url(r'^about/$', views.about , name="about"),
    url(r'^contact/$', views.contact , name="contact"),
    url(r'^school_calendar$', views.school_calendar , name="school_calendar"),
    url(r'^blog/$', views.blog , name="blog"),
    url(r'^test/$', views.test , name="test"),
    url(r'^training/$', views.training , name="training"),
]