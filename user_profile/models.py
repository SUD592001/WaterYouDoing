from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    username = models.CharField(max_length=30, null=False, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    weekly_laundry_loads = models.IntegerField(null=False)
    daily_bathroom_trips = models.IntegerField(null=False)
    weekly_showers = models.IntegerField(null=False)
    shower_times = models.IntegerField(null=False)
    weekly_baths = models.IntegerField(null=False)
    weekly_dishes = models.IntegerField(null=False)
    weekly_sprinkler = models.IntegerField(null=False)
    swimming_pool = models.BooleanField(null=False, default=False)
    score = models.IntegerField(null=False)

    def profile_url(self):
        return reverse('view_profile', kwargs={'username': self.username})

    def __str__(self):
        return self.username
