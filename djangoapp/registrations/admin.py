from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from registrations.models import Course, Student

@admin.register(Student)
class StudentAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("first_name", "last_name")}),)


admin.site.register(Course)
