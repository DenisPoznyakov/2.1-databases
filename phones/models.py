from django.db import models


class Phone(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)
