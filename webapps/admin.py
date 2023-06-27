from django.contrib import admin
from . import models
from webapps.models import Account
from django.contrib.auth.admin import UserAdmin

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender', 'birthdate')})
UserAdmin.fieldsets = tuple(fields)


admin.site.register(Account, UserAdmin)
admin.site.register(models.Article)
admin.site.register(models.Comment)
