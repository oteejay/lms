from django.db import models
from django.contrib.auth.models import User


from client.models import Client
from plant.models import Plant
from supplier.models import Supplier


# Create your models here.


def upload_location(instance, filename):
    return "%s/%s/%s" %(instance.client.acronym, 'master', filename)


class Master(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='masters')
	middle_name = models.CharField(max_length=20, blank=True, null=True)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	is_superior = models.BooleanField(default=False)
	phone = models.CharField(max_length=15)
	is_suspended = models.BooleanField(default=False)
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	image = models.ImageField(upload_to=upload_location, blank=True, null=True)
	modified_by = models.ForeignKey(User, 
			on_delete=models.DO_NOTHING, 
			blank=True, null=True, 
			related_name='modified_masters')
	invited_by = models.ForeignKey(User, 
			on_delete=models.DO_NOTHING, 
			blank=True, null=True, 
			related_name='invited_masters')
	plants = models.ManyToManyField(Plant, 
			through='MasterPlant', 
			through_fields=('master', 'plant'),
			related_name='masters')
	suppliers = models.ManyToManyField(Supplier, 
			through='MasterSupplier', 
			through_fields=('master', 'supplier'),
			related_name='masters')

	def full_name(self):
		if self.middle_name:
			return "{} {} {}".format(self.user.first_name, self.middle_name, self.user.last_name)
		else:
			return self.user.full_name()

	def __str__(self):
		return self.user.full_name()


class MasterPlant(models.Model):
	master = models.ForeignKey(Master, on_delete=models.CASCADE)
	plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class MasterSupplier(models.Model):
	master = models.ForeignKey(Master, on_delete=models.CASCADE)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

