from django import forms
from django.core.exceptions import ValidationError
from .models import UserModel
from django.utils.translation import gettext_lazy as _


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=16, label=_("Username"), min_length=3, widget=forms.TextInput(attrs={
        'placeholder': _('Enter your username')
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': _('youremailname@example.com')
    }))
    first_name = forms.CharField(max_length=25, label=_("First_name"))
    last_name = forms.CharField(max_length=25, label=_('Last_name'))
    password = forms.CharField(label=_("Password"), max_length=16, min_length=5, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label=_("Confirm password"), max_length=16, min_length=5,
                                       widget=forms.PasswordInput)

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError(_('Passwords are not the same!'))
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label=_("Username"), widget=forms.TextInput(attrs={
        'placeholder': _('username')
    }))
    password = forms.CharField(max_length=16, label=_("Password"), min_length=6, widget=forms.PasswordInput(attrs={
        'placeholder': _('Enter your password')
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
