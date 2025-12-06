from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Course, Student
from .forms import StudentRegistrationForm

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


class CourseCreateView(LoginRequiredMixin, generic.CreateView):
    model = Course
    fields = "__all__"
    template_name = 'registrations/course_form.html'
    success_url = reverse_lazy('registrations:course-list')


class CourseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Course
    fields = "__all__"
    template_name = 'registrations/course_form.html'
    success_url = reverse_lazy('registrations:course-list')


class CourseDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Course
    template_name = 'registrations/course_confirm_delete.html'
    success_url = reverse_lazy('registrations:course-list')


class StudentListView(LoginRequiredMixin, generic.ListView):
    model = Student
    paginate_by = 10


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Student
    form_class = StudentRegistrationForm
    template_name = 'registrations/student_form.html'
    success_url = reverse_lazy('registrations:student-list')
