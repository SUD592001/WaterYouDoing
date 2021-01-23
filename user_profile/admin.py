from django.contrib import admin
from user_profile import models

admin.site.site_title = 'Water U Doing'
admin.site.site_header = 'Water U Doing // Admin Portal'

# Register your models here.
@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    ordering = ['username']
    list_display = ['username', 'score']
    readonly_fields = ['score']
