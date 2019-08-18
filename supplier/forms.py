from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'acronym', 'coverage', 'ownership', 'address', 'phone', 'email')
        labels = {
            'address': _('Address'),
            'phone': _('Phone Number'),
            'email': _('Email Address')
        }
        help_texts = {
            'name': _('The name of the supplier.'),
            'acronym': _('The shorter form of this name to be used as unique identifier of the supplier.'),
            'ownership': _('The type of ownership or business.')
        }
        widgets = {
            'coverage': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'ownership': forms.Select(),
            'address': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }

