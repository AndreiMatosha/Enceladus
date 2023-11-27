from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50, unique=False, null=False, blank=False)
    country = models.CharField(max_length=50, unique=False, null=False, blank=False)


class Employee(models.Model):
    name = models.CharField(max_length=50, unique=False, null=False, blank=False)
    surname = models.CharField(max_length=50, unique=False, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    job_position = models.CharField(max_length=50, unique=False, null=False, blank=False)
    employer = models.ForeignKey(Company, on_delete=models.CASCADE)




