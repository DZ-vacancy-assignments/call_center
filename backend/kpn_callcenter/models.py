from django.db import models

from localflavor.nl.models import NLZipCodeField
from phonenumber_field.modelfields import PhoneNumberField


class TimeStamps(models.Model):
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)


class Customer(TimeStamps):
    FEMALE = 'female'
    MALE = 'male'
    OTHER = 'other'
    UNKNOWN = 'Unknown'

    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other'),
        (UNKNOWN, 'Unknown'),
    )

    last_name = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    date_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=UNKNOWN)

    house_number = models.CharField(max_length=10, null=True, blank=True)
    zip_code = NLZipCodeField(null=True, blank=True)
    street_name = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    telephone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    notes = models.CharField(max_length=1000, null=True, blank=True)
