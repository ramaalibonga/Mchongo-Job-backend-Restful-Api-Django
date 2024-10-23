from enum import unique
from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import AbstractUser

#job details 
class JobDetails(models.Model):
        category = [("PRIVATE","PRIVATE"),("GOVERNMENT","GOVERNMENT")]
        status_option = [("ACTIVE","ACTIVE"),("EXPIRED","EXPIRED")]
        job_title = models.CharField(max_length=255)
        job_category = models.CharField(max_length=255,choices=category)
        position = models.CharField(max_length=255)
        proffesional = models.CharField(max_length=255)
        job_description = models.TextField()
        start_date = models.DateField()
        ending_date = models.DateField()
        status = models.CharField(max_length=255,choices=status_option)
        address_id = models.ForeignKey("Address",on_delete=models.CASCADE)
        location_id = models.ForeignKey("Location",on_delete= models.CASCADE)
        created_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
        county_list = [("KENYA","KENYA"),("UGANDA","UGANDA")]
        city_list = [("DAR ES SALAAM","DAR ES SALAAM"),("RUVUMA","RUVUMA"),("MTWARA","MTWARA")]
        ward_list = [("ILALA","ILALA")]
        street_list = [("BARUTI","BARUTI"),("KONA","KONA")]
        country = models.CharField(max_length=255)
        city = models.CharField(max_length=100,choices=city_list)
        ward = models.CharField(max_length=100,choices=ward_list)
        street = models.CharField(max_length=100,choices=street_list)
        created_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
        latitude = models.DecimalField(decimal_places=6,max_digits=999999)
        longitude = models.DecimalField(decimal_places=6,max_digits=999999)
        created_at = models.DateTimeField(auto_now=True)


class AdminDetails(models.Model):
            pass

class UserAccount(AbstractUser):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)

class EmailList(models.Model):
        email = models.EmailField(unique=True)
        created_at = models.DateTimeField(auto_now=True)
        

