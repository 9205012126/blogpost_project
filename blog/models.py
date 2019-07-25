from django.db import models

# Create your models here.
class JobsConfig(models.Model):
    image = models.Imagefield(upload_to='images/')
    summary = models.Charfield(max_length=200)
