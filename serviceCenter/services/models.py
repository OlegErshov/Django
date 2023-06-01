from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='device/%Y/%m/%d', blank=True)

    device_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Issue(models.Model):
    issue_type = models.CharField(max_length=100)

    device_type = models.ForeignKey(Category, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.issue_type

class Client(models.Model):

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    date_of_birth = models.DateField()

    email = models.EmailField()

    phone_number = models.CharField(max_length=50,)

    def __str__(self):
        return self.email
