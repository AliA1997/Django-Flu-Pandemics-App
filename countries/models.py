from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=100)
    population = models.FloatField()
    population_in = models.CharField(max_length=30, default='thousands')
    def __str__(self):
        return f"{self.name}, {self.capital}"


class Religion(models.Model):
    name = models.CharField(max_length=50)
    population = models.FloatField()
    population_in = models.CharField(max_length=30, default='thousands')
    birth_place = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.FloatField()
    population_in = models.CharField(max_length=30, default='thousands')
    country = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

