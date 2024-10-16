from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="drivers")

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
