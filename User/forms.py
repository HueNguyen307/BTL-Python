from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import fields
from User.models import User
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'address' )
        widgets = {
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
            'phone_number':  NumberInput(attrs={'class': 'input', 'placeholder': 'phone_number'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
        }
