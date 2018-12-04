from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    #Meta inspects the current model of the class User, then ensures that 4 of the fields inside of it are there
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']