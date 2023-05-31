from django.db import models


class Device(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='не решил ещё', blank=True)

    TYPES = ["laptop",
             "phone",
             "PC",
             "tablet"]

    device_type = models.CharField(max_length=50, choices=TYPES)

class Client(models.Model):

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    date_of_birth = models.DateField()

    email = models.EmailField()

    phone_number = models.CharField(max_length=50,)
