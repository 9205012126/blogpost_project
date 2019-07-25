from django.db import models
from django.conf import settings

# Create your models here.
class Jobs(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
