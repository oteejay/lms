from django import  forms
from django.utils.translation import gettext_lazy as _


from .models import Agent, AgentPlant
from plant.models import Plant


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('middle_name', 'phone', 'image')
        labels = {
            'phone': _('Phone number'),
            'image': _('Profile picture')
        }


class AgentPlantForm(forms.ModelForm):
    plant = forms.ModelMultipleChoiceField(queryset=None, label='Plants')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(kwargs['initial']['agent'])
        self.fields['plant'].queryset = Plant.objects.all()
        # self.fields['plant'].queryset = Plant.objects.filter(client__pk=self.model.agent.supplier.masters.client.pk)

    class Meta:
        model = AgentPlant
        fields = ('agent', 'plant')
        widgets = {
            'agent': forms.HiddenInput
        }




# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'title', 'birth_date')
#         labels = {
#             'name': _('Writer'),
#         }
#         help_texts = {
#             'name': _('Some useful help text.'),
#         }
#         error_messages = {
#             'name': {
#                 'max_length': _("This writer's name is too long."),
#             },
#         }
#         widgets = {
#             'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#         }