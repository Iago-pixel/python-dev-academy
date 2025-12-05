from django.urls import path

from registrations.views import index, CourseListView, CourseDetailView, StudentListView, StudentDetailView

urlpatterns = [
    path("", index, name="index"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>", CourseDetailView.as_view(), name="course-detail"),
    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/<int:pk>", StudentDetailView.as_view(), name="student-detail"),
]

app_name = "registrations"
