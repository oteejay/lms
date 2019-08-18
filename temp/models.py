from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def upload_location(instance, filename):
    return "%s/%s/%s" %('jtgreen', 'temp', filename)


class TempUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tempusers')
    designation = models.CharField(max_length=15, 
            default='Installer',
            choices=[
                    ('Installer', 'Installer'),
                    ('Master', 'Master'),
                    ('Personel', 'Personel'),
                    ('Agent', 'Agent')
                ])
    used = models.BooleanField(default=False)
    cv = models.FileField(upload_to=upload_location, blank=True, null=True)


class Invitation(models.Model):
    email = models.EmailField()
    designation = models.CharField(max_length=15, 
            default='Installer',
            choices=[
                    ('Installer', 'Installer'),
                    ('Master', 'Master'),
                    ('Personel', 'Personel'),
                    ('Agent', 'Agent')
                ])
    used = models.BooleanField(default=False)
    token = models.CharField(max_length=254)
    inviter_id = models.IntegerField(blank=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_invitations')


class PasswordReset(models.Model):
    email = models.EmailField()
    used = models.BooleanField(default=False)
    token = models.CharField(max_length=254)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    

