from django.db import models

# Create your models here.
Class Name(models.Model):
    name = models.CharField(max_length=30, min_length=4, primary_key=True)

Class Score(models.Model):
    score = models.IntegerField(No=false)