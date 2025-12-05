from django.urls import path

from registrations.views import index, course_list

urlpatterns = [
    path("", index, name="index"),
    path("courses/", course_list, name="courses-list"),
]

app_name = "registrations"
