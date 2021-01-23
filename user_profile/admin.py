from django.contrib import admin
from user_profile import models

admin.site.site_title = 'Water U Doing'
admin.site.site_header = 'Water U Doing // Admin Portal'

# Register your models here.
admin.site.register(models.UserProfile)
