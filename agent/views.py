from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.contrib import messages

from .forms import AgentForm, AgentPlantForm
from temp.forms import UserForm

# Create your views here.

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        agent_form = AgentForm(request.POST)
        if user_form.is_valid() and agent_form.is_valid():
            user_form.save()
            agent_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        agent_form = AgentForm()
    return render(request, 'agent_create.html', {
        'user_form': user_form,
        'agent_form': agent_form
    })

def agent_plant_create(request, agent_pk):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        agent_form = AgentForm(request.POST)
        if user_form.is_valid() and agent_form.is_valid():
            user_form.save()
            agent_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = AgentPlantForm(request.POST or None, initial={'agent': agent_pk, 'plant': []})
    return render(request, 'agent_plant_create.html', {
        'form': form
    })
