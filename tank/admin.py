from django.contrib import admin

from .models import Tank, Configuration, Volume, SMS

# Register your models here.

admin.site.register(Tank)
admin.site.register(Configuration)
admin.site.register(Volume)
admin.site.register(SMS)
