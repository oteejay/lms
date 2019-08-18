from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Personel


# Create your views here.

class PersonelCreate(CreateView):
    model = Personel
    form_class = 
    fields = ['name']

class PersonelUpdate(UpdateView):
    model = Personel
    fields = ['name']

class PersonelDelete(DeleteView):
    model = Personel
    success_url = reverse_lazy('author-list')

