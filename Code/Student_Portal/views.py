from django.shortcuts import render
from django.http import HttpResponse
from Admin.models import Student,Attendance,Results
from django.template import loader

def login(request):
    return HttpResponse("<h1>Login1</h1>")

def profile(request , student_id):
    student = Student.objects.filter(id=student_id)
    context = {'student' : student[0]}
    return render(request , 'Student_Portal/profile.html', context)

def attendance(request , student_id):
    student = Student.objects.filter(id=student_id)
    attendance = Attendance.objects.filter(student_id=student[0], Year='2018')
    context = {'attendance' : attendance,
               'student' : student[0] }
    return render(request , 'Student_Portal/Attendance.html', context)

def results(request , student_id):
    student = Student.objects.filter(id=student_id)
    results = Results.objects.filter(student_id = student[0] )
    context = {'results' : results,
               'student' : student[0] }
    return render(request , 'Student_Portal/Results.html', context)