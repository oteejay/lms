from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Plant, State, LGA, Gen, Running

class PlantForm(forms.ModelForm):
    state = forms.ModelChoiceField(queryset=State.objects.all(), empty_label='...select state...')
    lga = forms.ModelChoiceField(queryset=LGA.objects.all(), empty_label='...select lga...')

    class Meta:
        model = Plant
        fields = ('plant_no', 'description', 'original_no', 'location', 'town_city', 'state', 'lga')
        labels = {
            'plant_no': _('Plant Number'),
            'original_no': _('Original Number'),
            'town_city': _('Town/City'),
            'lga': _('LGA')
        }
        help_texts = {
            'plant_no': _('A code number to be used to identify this plant on this LMS.'),
            'description': _('A helpful short description of this plant if it may be of help.'),
            'original_no': _('The original code number assigned to this plant by its owner if there is one.'),
            'town_city': _('The name of the cosmopolitan area (either town or city) that this plant is associated with.')
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'location': forms.Textarea(attrs={'cols': 40, 'rows': 4})
        }


class GenForm(forms.ModelForm):
    plant = forms.ModelChoiceField(queryset=Plant.objects.all(), empty_label='...select plant...')

    class Meta:
        model = Gen
        fields = ('plant', 'position', 'model_no', 'brand')
        labels = {
            'model_no': _('Model'),
            'brand': _('Manufacturer')
        }
        help_texts = {
            'plant': _('The plant, this generator is located in.'),
            'position': _('Whether this generator is Gen 1, Gen 2, ...'),
            'model_no': _("The manufacturer's assigned model code number.")
        }
        widgets = {
            'position': forms.Select()
        }

