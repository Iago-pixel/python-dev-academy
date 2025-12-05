from django.urls import path

from registrations.views import index, CourseListView, CourseDetailView

urlpatterns = [
    path("", index, name="index"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>", CourseDetailView.as_view(), name="course-detail"),
]

app_name = "registrations"
