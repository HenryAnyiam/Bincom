from django import forms
from .models import User, Task


class UserSignUpForm(forms.ModelForm):
    """signup a new user"""

    class Meta:
        model = User
        fields = ["username", "email", "password"]

        widgets = {
                "password": forms.PasswordInput()
                }


class TaskCreateForm(forms.ModelForm):
    """create a new Task"""

    class Meta:
        model = Task
        exclude = ["id", "created_at"]
