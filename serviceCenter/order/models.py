from django.db import models

# Create your models here.
from django.db import models
from services.models import Issue, Client
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Enter product cost",
        validators=[MinValueValidator(Decimal("0.01"))],
        default=0
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


    def __str__(self):
        return f"Order {self.id}, created on {self.creation_date}."

    def get_total_cost(self):
        return sum(item.get_total_cost() for item in self.items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id}"

    def get_total_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if self.issue:
            self.price = self.issue.price

        super().save(*args, **kwargs)
