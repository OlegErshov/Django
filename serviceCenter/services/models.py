from django.db import models
from django.urls import reverse

class Device_type(models.Model):

    # класс для типа товара, ноутбук, планшет, телефон, пк, наушники, и для них виды услуг из Issue
    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='static/services/img/', blank=True)

    def __str__(self):
        return self.name



class Issue(models.Model):

    # класс для услу к примеру чистка от пыли, замена термопасты, ремонт, замена экрана и т.д
    issue_type = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10,decimal_places=2)

    device_type = models.ForeignKey(Device_type
                                    , on_delete=models.CASCADE)

    count = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def get_absolute_url(self):
        return reverse('services:detail', args=[str(self.id)])
    def __str__(self):
        return self.issue_type



class Client(models.Model):

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    date_of_birth = models.DateField()

    email = models.EmailField()

    phone_number = models.CharField(max_length=50,)

    image = models.ImageField(upload_to='static/services/img/', blank=True)

    def __str__(self):
        return self.email

class News(models.Model):
    image = models.ImageField(upload_to='static/services/img/', blank=True)
    name = models.CharField(null=False,max_length=300)
    description = models.CharField(null=False,max_length=80)
    full_text = models.CharField(null=False,max_length=1000)
    def __str__(self):
        return self.name

class FeedBack(models.Model):
    client = models.ForeignKey(Client
                                    , on_delete=models.CASCADE)
    text = models.TextField(null = False, max_length=350)

    mark = models.DecimalField(null = False,decimal_places=0,max_digits=1)

    image = models.FileField(upload_to='static/services/img/', blank=True)

    time = models.TimeField(null= False)

class Stuff(models.Model):
    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    date_of_birth = models.DateField()

    email = models.EmailField()

    phone_number = models.CharField(max_length=50, )

    image = models.ImageField(upload_to='static/services/img/', blank=True)

    job_description = models.CharField(max_length=1000)