from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'acronym', 'ownership', 'address', 'phone', 'email')
        labels = {
            'address': _('Address'),
            'phone': _('Phone Number'),
            'email': _('Email Address')
        }
        help_texts = {
            'name': _('The name of the client.'),
            'acronym': _('The shorter form of this name to be used as unique identifier of the client.'),
            'ownership': _('The type of ownership or business.')
        }
        widgets = {
            'ownership': forms.Select(),
            'address': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }

