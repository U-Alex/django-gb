from django.db import models
from datetime import datetime


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True, blank=True)
    address = models.TextField(blank=True)
    date_reg = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return f"{self.id} | {self.name} | {self.email} | {self.phone} | {self.address} | {self.date_reg}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    date_add = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return f"{self.id} | {self.name} | {self.description} | {self.price} | {self.quantity} | {self.date_add}"


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.status_name}"


class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, default=1)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    product = models.ManyToManyField(Product, through='Trash')
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return f"{self.id} | {self.status} | {self.client.name} | {self.total_amount} | {self.date_order}"

    def get_total_amount(self):
        total = 0
        for rec in Trash.objects.filter(order=self):
            total += (rec.quantity * rec.product.price)
        return total


class Trash(models.Model):
    """промежуточная модель для использования дополнительных полей"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_add = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return f"{self.id} | {self.product.name} | {self.order.id} | {self.quantity} | {self.date_add}"