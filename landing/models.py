from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse


class UserProfile(models.Model):
    shower_head_choices = [
        ("normal", "Normal shower head"),
        ("efficient", "Efficient shower head"),
    ]

    washer_type_choices = [
        ("top", "Top-load washer"),
        ("front", "Front-load washer"),
    ]

    swimming_pool_choices = [
        ("none", "No pool"),
        ("small", "Small pool"),
        ("medium", "Medium pool"),
        ("large", "Large pool"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, unique=True)
    score = models.IntegerField(null=False)
    weekly_laundry_loads = models.IntegerField(null=False)
    daily_bathroom_trips = models.IntegerField(null=False)
    weekly_showers = models.IntegerField(null=False)
    shower_times = models.IntegerField(null=False)
    weekly_baths = models.IntegerField(null=False)
    weekly_dishes = models.IntegerField(null=False)
    weekly_sprinkler = models.IntegerField(null=False)

    shower_head = models.CharField (
        max_length = 30,
        null=False,
        choices = shower_head_choices,
    )
    washer_type = models.CharField (
        max_length = 30,
        null=False,
        choices = washer_type_choices,
    )
    swimming_pool = models.CharField (
        max_length = 30,
        null=False,
        choices = swimming_pool_choices
    )

    def result_url(self):
        return reverse('result', kwargs={'username': self.user.username})

    def save(self, *args, **kwargs):
        self.score = 0
        self.score += self.daily_bathroom_trips * settings.TOILET_FLUSH * 7
        self.score += self.weekly_baths * settings.BATHTUB_FILL 
        self.score += self.weekly_dishes * settings.DISHWASHER_CYCLE 
        self.score += self.weekly_sprinkler * settings.SPRINKLER_MINUTE

        if self.shower_head == "normal" :
            self.score += self.weekly_showers * self.shower_times * settings.NORMAL_SHOWER_MINUTE 
        if self.shower_head == "efficient" :
            self.score += self.weekly_showers * self.shower_times * settings.EFFICIENT_SHOWER_MINUTE 

        if self.washer_type == "top":
            self.score += self.weekly_laundry_loads * settings.TOP_LOAD_WASHER_LOAD

        if self.washer_type == "front" :
            self.score += self.weekly_laundry_loads * settings.FRONT_LOAD_WASHER_LOAD

        if self.swimming_pool :
            if self.swimming_pool == "small" :
                self.score = self.score + settings.SWIMMING_POOL_SMALL
            if self.swimming_pool == "medium" :
                self.score = self.score + settings.SWIMMING_POOL_MEDIUM
            if self.swimming_pool == "large" :
                self.score = self.score + settings.SWIMMING_POOL_LARGE

        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username
