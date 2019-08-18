from django import  forms
from django.utils.translation import gettext_lazy as _


from .models import Master


class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ('middle_name', 'phone', 'image')
        labels = {
            'middle_name': _('Middle Name'),
            'phone': _('Phone Number'),
            'image': _('Profile Picture')
        }

