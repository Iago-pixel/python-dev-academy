from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from python_dev_academy import settings


class Student(AbstractUser):
    class Meta:
        ordering = ["first_name", "last_name", "id"]

    def get_absolute_url(self):
        return reverse("registrations:student-detail", args=[str(self.id)])


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="courses")

    class Meta:
        ordering = ["title", "id"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("registrations:course-detail", args=[str(self.id)])
