from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from Admin.models import Student,Attendance,Results,Login
from django.template import loader
from django.http import Http404

def login(request):
    return HttpResponse("<h1>Login1</h1>")

def profile(request):
    try:
        student_id = request.session['student_id']
    except KeyError:
        raise Http404("You have to Login First")
    student = get_object_or_404(Student, id=student_id);
    context = {'student' : student}
    return render(request , 'Student_Portal/profile.html', context)

def attendance(request):
    try:
        student_id = request.session['student_id']
    except KeyError:
        raise Http404("You have to Login First")
    student = get_object_or_404(Student, id=student_id)
    attendance = Attendance.objects.filter(student_id=student, Year='2018')
    cl_at = 0
    cl_t = 0
    for at in attendance:
        cl_at = cl_at + at.Class_Attended
        cl_t  = cl_t  + at.Total_Classes
    a_p = ((cl_at * 100 )/cl_t)
    a_p = "{0:.2f}".format(a_p)
    context = {'attendance' : attendance,
               'student' : student,
               'a_p' : a_p}
    return render(request , 'Student_Portal/Attendance.html', context)

def results(request):
    try:
        student_id = request.session['student_id']
    except KeyError:
        raise Http404("You have to Login First")
    student = get_object_or_404(Student, id=student_id)
    results = Results.objects.filter(student_id = student )
    context = {'results': results,
               'student': student }
    return render(request , 'Student_Portal/Results.html', context)

def check_session(request):
    student = get_object_or_404(Student, id=request.POST["username"])
    log = Login.objects.filter(student_id = student)
    if log[0].password == request.POST["password"]:
        request.session["student_id"]=request.POST["username"]
        return redirect('Student_Portal:profile')
    else:
        return HttpResponse("<h1>Invalid Credentials</h1>")

def logout(request):
    del request.session["student_id"]
    return redirect('Blog:index')