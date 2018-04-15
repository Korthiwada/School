from django.contrib import admin
from .models import Student,Class,Login,Results,TotalMarks,Attendance
# Register your models here.
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Login)
admin.site.register(Results)
admin.site.register(TotalMarks)
admin.site.register(Attendance)