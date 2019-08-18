from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=15, unique=True)
    ownership = models.CharField(max_length=20, 
            default="Corporate",
            choices=[
                    ('Corporate', 'Corporate'),
                    ('Private', 'Private'),
                    ('Neither', 'Neither')
                ])
    coverage = models.TextField(max_length=500)
    address = models.TextField(max_length=500)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_by = models.ForeignKey(User, 
            on_delete=models.DO_NOTHING, 
            blank=True, null=True, 
            related_name='modified_suppliers')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_suppliers')

