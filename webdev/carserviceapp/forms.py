from django import forms
from django.contrib.auth.forms import UserCreationForm

from carserviceapp.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Required')

    class Meta:
        model = User
        fields = ['email','first_name','last_name','phone_number','password1','password2']