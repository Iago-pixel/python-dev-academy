from django.urls import path

from registrations.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "registrations"
