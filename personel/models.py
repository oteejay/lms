from django.db import models
from django.contrib.auth.models import User


from plant.models import Plant
from master.models import Master


# Create your models here.


def upload_location(instance, filename):
    return "%s/%s/%s" %(instance.master.client.acronym, 'personel', filename)


class Personel(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='personels')
	middle_name = models.CharField(max_length=20, blank=True, null=True)
	master = models.ForeignKey(Master, on_delete=models.CASCADE)
	phone = models.CharField(max_length=15)
	is_suspended = models.BooleanField(default=False)
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	image = models.ImageField(upload_to=upload_location, blank=True, null=True)
	modified_by = models.ForeignKey(User, 
			on_delete=models.DO_NOTHING, 
			blank=True, null=True,
			related_name='modified_personels')
	invited_by = models.ForeignKey(User, 
			on_delete=models.DO_NOTHING, 
			blank=True, null=True,
			related_name='invited_personels')
	plants = models.ManyToManyField(Plant, 
			through='PersonelPlant', 
			through_fields=('personel', 'plant'),
			related_name='personels')

	def full_name(self):
		if self.middle_name:
			return "{} {} {}".format(self.user.first_name, self.middle_name, self.user.last_name)
		else:
			return self.user.full_name()

	def __str__(self):
		return self.user.full_name()


class PersonelPlant(models.Model):
	personel = models.ForeignKey(Personel, on_delete=models.CASCADE)
	plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

