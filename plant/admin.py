from django.contrib import admin

from .models import Plant, Gen, Running

# Register your models here.

admin.site.register(Plant)
admin.site.register(Gen)
admin.site.register(Running)
