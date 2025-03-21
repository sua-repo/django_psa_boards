from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# dev_15
# 이메일 필드가 없으면 입력하지 않아도 가능
#
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
