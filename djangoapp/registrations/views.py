from django.shortcuts import render

from .models import Course, Student

def index(request):
    num_courses = Course.objects.count()
    num_students = Student.objects.count()
    context = {
        "num_courses": num_courses,
        "num_students": num_students,
    }
    return render(request=request, template_name="registrations/index.html", context=context)
