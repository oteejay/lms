from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from client.models import Client

# Create your models here.


class Plant(models.Model):
    plant_no = models.CharField(max_length=20)
    description = models.TextField(max_length=600, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='plants')
    original_no = models.CharField(max_length=20, blank=True)
    location = models.TextField(max_length=300)
    town_city = models.CharField(max_length=20, verbose_name='Town/City')
    state = models.ForeignKey('State', on_delete=models.DO_NOTHING, related_name='plants')
    lga = models.ForeignKey('LGA', 
            on_delete=models.DO_NOTHING, 
            related_name='plants', 
            verbose_name='LGA')
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_by = models.ForeignKey(User, 
            on_delete=models.DO_NOTHING, 
            blank=True, null=True, 
            related_name='modified_plants')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_plants')

    def __str__(self):
        return "{} {}".format(self.client.acronym, self.plant_no)


class Gen(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='gens')
    position = models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    model_no = models.CharField(max_length=30, blank=True)
    brand = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "{} Gen{}".format(self.plant, self.position)

    class Meta:
        ordering = ['plant__plant_no', 'position']
        verbose_name = _('Generator')
        verbose_name_plural = _('Generators')


class Running(models.Model):
    gen = models.ForeignKey(Gen, on_delete=models.CASCADE, related_name='runnings')
    running = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        if self.running:
            return 1
        else:
            return 0

    class Meta:
        ordering = ['-time']
        verbose_name_plural = _('Running')







    




class State(models.Model):
    name = models.CharField(max_length=20)
    capital = models.CharField(max_length=20)
    extra_info = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class LGA(models.Model):
    name = models.CharField(max_length=30)
    headquarters = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='lgas')
    extra_info = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

