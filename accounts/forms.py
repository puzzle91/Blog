from django import forms
from django.contrib.auth.forms import UserCreationForm



class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )    