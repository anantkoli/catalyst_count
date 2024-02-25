from django.db import models


# Create your models here.
class File(models.Model):
    existingPath = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)
    eof = models.BooleanField()


class Company(models.Model):
    name = models.CharField(max_length=1000)
    domain = models.CharField(max_length=500)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=500)
    size = models.CharField(max_length=100)
    locality = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    linkedin_url = models.CharField(max_length=500)
    current_employees = models.IntegerField()
    total_employee = models.IntegerField()

