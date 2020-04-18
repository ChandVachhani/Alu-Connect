from django.contrib import admin
from .models import roles,projects,user_profile
# Register your models here.

admin.site.register(roles)
admin.site.register(projects)
admin.site.register(user_profile)