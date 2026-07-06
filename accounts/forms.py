from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    avatar = forms.ImageField(required=True, label="Аватар")
    email = forms.EmailField(required=True, label="Электронная почта")  # это обязательно оставить

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "avatar",
            "password1",
            "password2",
            "first_name",
            "bio",
            "phone",
            "gender",
        )