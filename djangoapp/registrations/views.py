from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course, Student

@login_required
def index(request):
    num_courses = Course.objects.count()
    num_students = Student.objects.count()
    context = {
        "num_courses": num_courses,
        "num_students": num_students,
    }
    return render(request=request, template_name="index.html", context=context)


class CourseListView(LoginRequiredMixin, generic.ListView):
    model = Course
    paginate_by = 10


class CourseDetailView(LoginRequiredMixin, generic.DetailView):
    model = Course


class StudentListView(LoginRequiredMixin, generic.ListView):
    model = Student
    paginate_by = 10


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student
