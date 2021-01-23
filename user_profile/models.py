from django.db import models
from django.conf import settings
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

    def save(self, *args, **kwargs):
        self.score = self.weekly_laundry_loads * settings.TOP_LOAD_WASHER_LOAD
        self.score += daily_bathroom_trips * settings.TOILET_FLUSH 
        self.score += weekly_showers * shower_times * settings.NORMAL_SHOWER_MINUTE 
        self.score += weekly_baths * settings.BATHTUB_FILL 
        self.score += weekly_dishes * settings.DISHWASHER_CYCLE 
        self.score += weekly_sprinkler * settings.SPRINKLER_MINUTE #total water usage
        if self.swimming_pool :
            self.score = self.score + settings.SWIMMING_POOL_FILL
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
