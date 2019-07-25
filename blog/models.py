from django.db import models

# Create your models here.


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=824)
    blog_date = models.DateField(auto_now=False,auto_now_add=False)
