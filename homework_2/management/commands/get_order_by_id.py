from django.core.management.base import BaseCommand
from ...models import Order, Basket


class Command(BaseCommand):
    help = "get_order_by_id"

    def add_arguments(self, parser):
        parser.add_argument('ord_id', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        order = Order.objects.filter(pk=kwargs['ord_id']).last()
        if order:
            trash = Basket.objects.filter(order=order).values()

            self.stdout.write(f"order: {order}\ntrash: {trash}")

        else:
            self.stdout.write(f'order not found')
