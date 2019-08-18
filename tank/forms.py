from django import  forms
from django.utils.translation import gettext_lazy as _


from plant.models import Plant
from .models import Tank, Configuration


class TankForm(forms.ModelForm):
    plant = forms.ModelChoiceField(queryset=Plant.objects.all(), empty_label='...select plant...')

    class Meta:
        model = Tank
        fields = ('plant', 'capacity', 'unit', 'image')
        help_texts = {
            'plant': _('The plant, this tank is located in.'),
            'unit': _('The unit of measurement for its capacity.'),
            'image': _("A picture of the scene where the LMS device is installed.")
        }


class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = ('shape', 'width', 'length', 'height', 'major_diameter', 
                        'minor_diameter', 'diameter', 'unit', 'alignment')
        labels = {
            'major_diameter': _('Major Diameter'),
            'minor_diameter': _('Minor Diameter')
        }
        help_texts = {
            'unit': _('The unit of measurement utilized for this configuration.')
        }
        widgets = {
            'shape': forms.Select(),
            'alignment': forms.Select()
        }

