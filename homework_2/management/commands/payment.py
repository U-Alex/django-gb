from django.core.management.base import BaseCommand
from django.db import transaction
from ...models import Order, Basket


class Command(BaseCommand):
    help = "payment"

    def add_arguments(self, parser):
        parser.add_argument('cl_id', type=int, help='User ID')
        parser.add_argument('ord_id', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        check_quantity = []
        with transaction.atomic():
            order = Order.objects.filter(pk=kwargs['ord_id'], client_id=kwargs['cl_id']).last()
            if order:
                for rec in Basket.objects.filter(order=order):
                    if rec.quantity > rec.product.quantity:
                        check_quantity.append([rec.product.name, rec.quantity - rec.product.quantity])

                if not len(check_quantity):
                    pass
                    """ списание товара со склада 
                        оплата
                        смена статуса заказа
                    """
                else:
                    self.stdout.write(f'not enough products: {check_quantity}')
            else:
                self.stdout.write(f'order not found')

