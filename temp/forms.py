from django import  forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


from .models import TempUser, Invitation, PasswordReset


class TempUserForm(forms.ModelForm):
    class Meta:
        model = TempUser
        fields = ('cv',)
        labels = {
            'cv': _('CV')
        }
        help_texts = {
            'cv': _('Your updated CV/resume could be needed.')
        }
        widgets = {
            'id': forms.HiddenInput,
            'cv': forms.ClearableFileInput
        }


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ('email',)
        help_texts = {
            'email': _('The email of the person you would like to send an invitation to.')
        }
        widgets = {
            'id': forms.HiddenInput
        }


class PasswordResetForm(forms.ModelForm):
    class Meta:
        model = PasswordReset
        fields = ('email',)
        help_texts = {
            'email': _('Your email which serves as your username on JT Green.')
        }
        widgets = {
            'id': forms.HiddenInput
        }


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'first_name', 'last_name')
        labels = {
            'username': _('Email')
        }
        help_texts = {
            'username': _('Your email will be set as your username on JT Green.')
        }
        widgets = {
            'password': forms.PasswordInput
        }
        
