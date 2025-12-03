from django.db import models
from django.contrib.auth.models import AbstractUser

from python_dev_academy import settings


class Student(AbstractUser):
    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return self.first_name + " " + self.last_name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="courses")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
