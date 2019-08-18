from django.contrib import admin

from .models import Master, MasterPlant, MasterSupplier

# Register your models here.

admin.site.register(Master)
admin.site.register(MasterPlant)
admin.site.register(MasterSupplier)
