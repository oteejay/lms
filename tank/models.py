from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


from plant.models import Plant


# Create your models here.


def upload_location(instance, filename):
    return "%s/%s/%s" %(instance.plant.client.acronym, 'tank', filename)


class Tank(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE)
    configuration = models.OneToOneField('Configuration', 
            on_delete=models.CASCADE, 
            blank=True, null=True)
    capacity = models.FloatField(blank=True, default=0)
    unit = models.CharField(max_length=15, default='liter', blank=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    modified_by = models.ForeignKey(User, 
            on_delete=models.DO_NOTHING, 
            blank=True, null=True, 
            related_name='modified_tanks')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_tanks')

    def __str__(self):
        return "{} Tank".format(self.plant)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Configuration(models.Model):
    shape = models.CharField(max_length=20, 
            default='Cylinderical',
            choices=[
                    ('Cylinderical', 'Cylinderical'),
                    ('Rectangular', 'Rectangular'),
                    ('Elliptical', 'Elliptical'),
                    ('Other', 'Other')
                ])
    width = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    major_diameter = models.FloatField(blank=True, null=True)
    minor_diameter = models.FloatField(blank=True, null=True)
    diameter = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=15, default='meter', blank=True)
    alignment = models.CharField(max_length=15, 
            default='Horiontal',
            choices=[
                    ('Horizontal', 'Horizontal'),
                    ('Vertical', 'Vertical'),
                    ('Neither', 'Neither')
                ])
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_by = models.ForeignKey(User, 
            on_delete=models.DO_NOTHING, 
            blank=True, null=True, 
            related_name='modified_configurations')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_configurations')


class Volume(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, related_name='volumes')
    volume = models.FloatField()
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.volume

    class Meta:
        ordering = ['-time']
        verbose_name_plural = _('Volume')


class SMS(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, related_name='smses')
    sender = models.CharField(max_length=30)
    text = models.TextField(max_length=600)
    date_received = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.sender

    class Meta:
        ordering = ['-date_received']
        verbose_name_plural = _('SMS')

