from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=30, null=False, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=False)

    def __str__(self):
        return self.username
