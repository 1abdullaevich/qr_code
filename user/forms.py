from django import forms
from django.core.exceptions import ValidationError
from .models import UserModel


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=16, min_length=3, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'youremailname@example.com'
    }))
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    password = forms.CharField(max_length=16, min_length=5, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=16, min_length=5, widget=forms.PasswordInput)

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('Passwords are not the same!', 'confirm_password')
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'username'
    }))
    password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password'
    }))

# class LoginForm(forms.ModelForm):
#
#     class Meta:
#         model = UserModel
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'placeholder': 'Enter your username'
#             }),
#             'password': forms.TextInput(attrs={
#                 'placeholder': 'Enter your password'
#             })
#         }
