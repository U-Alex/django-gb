from django.core.management.base import BaseCommand
from ...models import Client, Product, OrderStatus, Order, Trash
from random import randint, choice


class Command(BaseCommand):
    help = "fake data"

    def handle(self, *args, **kwargs):

        # OrderStatus.objects.create(status_name='new')
        # OrderStatus.objects.create(status_name='paid')
        # OrderStatus.objects.create(status_name='delivery')
        # OrderStatus.objects.create(status_name='cancelled')
        #
        # for i in range(10):
        #     Client.objects.create(name=f"user_{i+1}",
        #                           email=f"user_{i+1}@mail.com",
        #                           phone=f"+7800{randint(1000000, 9999999)}",
        #                           address="Russia",
        #                           )
        # self.stdout.write(f'create {Client.objects.count()} clients')
        #
        # for i in range(50):
        #     Product.objects.create(name=f"product_{i+1}",
        #                            description=f"product_{i+1} description",
        #                            price=randint(1, 9999),
        #                            quantity=randint(1, 99),
        #                            )
        # self.stdout.write(f'create {Product.objects.count()} products')

        ord_status = OrderStatus.objects.all()
        clients = Client.objects.all()
        products = Product.objects.all()

        for i in range(20):
            Order.objects.create(status=choice(ord_status), client=choice(clients), total_amount=0)

        orders = Order.objects.all()
        for order in orders:
            for i in range(10):
                product = choice(products)
                trash = Trash.objects.filter(order_id=order.id, product_id=product.id).last()
                if trash:
                    trash.quantity += 1
                    trash.save()
                else:
                    new_trash = Trash(product=product,
                                      order=order,
                                      date_add=f"2024-01-{randint(0, 2)}{randint(1, 8)}",
                                      )
                    new_trash.save()
            order.total_amount = order.get_total_amount()
            order.save()


