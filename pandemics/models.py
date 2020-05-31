from django.db import models

# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=75)
    type = models.CharField(max_length=100)
    average_mortality_rate = models.FloatField()
    def __str__(self):
        return f"{self.name}"


class Pandemic(models.Model):
    name = models.CharField(max_length=75)
    disease = models.CharField(max_length=75)
    total_deaths = models.IntegerField()
    year_from = models.IntegerField()
    year_to = models.IntegerField()
    embed_html = models.CharField(max_length=3000)
    def __str__(self):
        return f"{self.name} {self.year_from} - {self.year_to}"
