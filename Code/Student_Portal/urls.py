from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'Student_Portal'

urlpatterns = [
    url(r'^$', views.login, name="login"),
    # url(r'^/check/(?P<student_id>[0-9]+)/$', views.check_session, name="check"),
    url(r'^/check/$', views.check_session, name="check"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^Attendance$', views.attendance, name="attendance"),
    url(r'^Results$', views.results, name="results"),
    url(r'^logout$', views.logout, name="logout")
]