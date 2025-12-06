from django.urls import path

from registrations.views import index, CourseListView, CourseDetailView, StudentListView, StudentDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>", CourseDetailView.as_view(), name="course-detail"),
    path("courses/create", CourseCreateView.as_view(), name="course-create"),
    path("courses/<int:pk>/update", CourseUpdateView.as_view(), name="course-update"),
    path("courses/<int:pk>/delete", CourseDeleteView.as_view(), name="course-delete"),
    path("students/", StudentListView.as_view(), name="student-list"),
    path("students/<int:pk>", StudentDetailView.as_view(), name="student-detail"),
]

app_name = "registrations"
