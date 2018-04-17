from django.shortcuts import render

def index(request):
    return render(request, "Blog/index.html" , {})

def about(request):
    return render(request, "Blog/about.html" , {})

def admission(request):
    return render(request, "Blog/admissions.html" , {})

def blog(request):
    return render(request, "Blog/blog.html" , {})

def career(request):
    return render(request, "Blog/career.html" , {})

def contact(request):
    return render(request, "Blog/contact-us.html" , {})

def school_calendar(request):
    return render(request, "Blog/school-calendar.html" , {})

def test(request):
    return render(request, "Blog/test.html" , {})

def training(request):
    return render(request, "Blog/training-courses.html" , {})