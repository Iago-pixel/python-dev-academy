from django.urls import path

from registrations.views import index, CourseListView

urlpatterns = [
    path("", index, name="index"),
    path("courses/", CourseListView.as_view(), name="courses-list"),
]

app_name = "registrations"
