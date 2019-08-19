from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from plant.models import Plant
from supplier.models import Supplier


# Create your models here.


def upload_location(instance, filename):
    return "%s/%s/%s" %(instance.supplier.acronym, 'supplier', filename)


class Agent(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='agents')
	middle_name = models.CharField(max_length=20, blank=True, null=True)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	is_superior = models.BooleanField(default=False)
	phone = models.CharField(max_length=15)
	is_suspended = models.BooleanField(default=False)
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	image = models.ImageField(upload_to=upload_location, blank=True, null=True)
	modified_by = models.ForeignKey(User, 
			on_delete=models.DO_NOTHING, 
			blank=True, null=True, 
			related_name='created_agents')
	invited_by = models.ForeignKey(User, 
			on_delete=models.DO_NOTHING, 
			blank=True, null=True, 
			related_name='invited_agents')
	plants = models.ManyToManyField(Plant, 
			through='AgentPlant', 
			through_fields=('agent', 'plant'),
			related_name='agents')

	def full_name(self):
		if self.middle_name:
			return "{} {} {}".format(self.user.first_name, self.middle_name, self.user.last_name)
		else:
			return self.user.full_name()

	def __str__(self):
		return self.user.full_name()


class AgentPlant(models.Model):
	agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
	plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Agent.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()

