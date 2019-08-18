from django import  forms
from django.utils.translation import gettext_lazy as _


from .models import Personel
from plant.models import Plant


class PersonelForm(forms.ModelForm):
    class Meta:
        model = Personel
        fields = ('middle_name', 'phone', 'image')
        labels = {
            'middle_name': _('Middle Name'),
            'phone': _('Phone Number'),
            'image': _('Profile Picture')
        }


class PersonelPlantForm(forms.ModelForm):
    plant = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plant'].queryset = Plant.objects.filter(client__pk=self.model.master.client.pk)

    class Meta:
        model = Personel
        fields = ('plant',)

