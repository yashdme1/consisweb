from django import forms
from .models import Role

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    designation = forms.CharField(max_length=100, label='Designation')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        label='Role',
        widget=forms.Select,
        required=True
    )

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
