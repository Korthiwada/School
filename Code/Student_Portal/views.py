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
    cl_at = 0
    cl_t = 0
    for at in attendance:
        cl_at = cl_at + at.Class_Attended
        cl_t  = cl_t  + at.Total_Classes
    a_p = ((cl_at * 100 )/cl_t)
    a_p = "{0:.2f}".format(a_p)
    context = {'attendance' : attendance,
               'student' : student[0],
               'a_p' : a_p}
    return render(request , 'Student_Portal/Attendance.html', context)

def results(request , student_id):
    student = Student.objects.filter(id=student_id)
    results = Results.objects.filter(student_id = student[0] )
    context = {'results' : results,
               'student' : student[0] }
    return render(request , 'Student_Portal/Results.html', context)