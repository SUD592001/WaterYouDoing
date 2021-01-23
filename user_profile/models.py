from django.db import models
from django.conf import settings
from django.urls import reverse


class UserProfile(models.Model):
    username = models.CharField(max_length=30, null=False, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=False)

    def profile_url(self):
        return reverse('view_profile', kwargs={'username': self.username})

    def save(self):
        score = 0 #whatever
        super.save()
        self.score = 0; #total water usage

    def __str__(self):
        return self.username
