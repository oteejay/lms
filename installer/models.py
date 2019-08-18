from django.db import models
from django.contrib.auth.models import User


# Create your models here.


def upload_location(instance, filename):
    return "%s/%s/%s" %('jtgreen', 'installer', filename)


class Installer(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	middle_name = models.CharField(max_length=20, blank=True, null=True)
	address = models.TextField(max_length=500)
	phone = models.CharField(max_length=15)
	staff_id = models.CharField(max_length=10, blank=True, null=True)
	position = models.CharField(max_length=20, 
			default='Unspecified',
			choices=[
					('Engineer', 'Engineer'),
					('Technician', 'Technician'),
					('Support', 'Support'),
					('Rep', 'Rep'),
					('Unspecified', 'Unspecified')
				])
	is_suspended = models.BooleanField(default=False)
	last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	image = models.ImageField(upload_to=upload_location, blank=True, null=True)
	modified_by = models.ForeignKey(User, 
			on_delete=models.DO_NOTHING, 
			blank=True, null=True, 
			related_name='modified_installers')
	invited_by = models.ForeignKey(User, 
			on_delete=models.DO_NOTHING, 
			blank=True, null=True,
			related_name='invited_installers')

	def full_name(self):
		if self.middle_name:
			return "{} {} {}".format(self.user.first_name, self.middle_name, self.user.last_name)
		else:
			return self.user.full_name()

	def __str__(self):
		return self.user.full_name()
