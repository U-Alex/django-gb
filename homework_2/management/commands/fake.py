from django.core.management.base import BaseCommand
from ...models import Client, Product, OrderStatus
from random import randint


class Command(BaseCommand):
    help = "fake data"

    def handle(self, *args, **kwargs):

        OrderStatus.objects.create(status_name='new')
        OrderStatus.objects.create(status_name='paid')
        OrderStatus.objects.create(status_name='delivery')
        OrderStatus.objects.create(status_name='cancelled')

        for i in range(10):
            Client.objects.create(name=f"user_{i+1}",
                                  email=f"user_{i+1}@mail.com",
                                  phone=f"+7800{randint(1000000, 9999999)}",
                                  address="Russia",
                                  )
        self.stdout.write(f'create {Client.objects.count()} clients')

        for i in range(100):
            Product.objects.create(name=f"product_{i+1}",
                                   description=f"product_{i+1} description",
                                   price=randint(1, 9999),
                                   quantity=randint(1, 99),
                                   )
        self.stdout.write(f'create {Product.objects.count()} products')


