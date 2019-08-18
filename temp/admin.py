from django.contrib import admin

from .models import TempUser, Invitation, PasswordReset

# Register your models here.

admin.site.register(TempUser)
admin.site.register(Invitation)
admin.site.register(PasswordReset)
