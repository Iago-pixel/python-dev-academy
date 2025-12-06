from django.contrib.auth.forms import UserCreationForm

from .models import Student


class StudentRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email",)
