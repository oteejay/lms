from django import  forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


from .models import Installer


class InstallerForm(forms.ModelForm):
    class Meta:
        model = Installer
        fields = ('middle_name', 'address', 'phone', 'image')
        labels = {
            'middle_name': _('Middle Name'),
            'phone': _('Phone Number'),
            'image': _('Profile Picture')
        }
        widgets = {
            'address': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }
        
