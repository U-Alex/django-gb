from django.core.management.base import BaseCommand
from ...models import Client, Product, Order, Trash


class Command(BaseCommand):
    help = "del_prod_from_order"

    def add_arguments(self, parser):
        parser.add_argument('cl_id', type=int, help='User ID')
        parser.add_argument('ord_id', type=int, help='Order ID')
        parser.add_argument('prod_id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs['cl_id'])
        order = Order.objects.filter(pk=kwargs['ord_id'], client=client).first()
        if not order:
            self.stdout.write(f'order not found')
            return

        product = Product.objects.get(pk=kwargs['prod_id'])
        trash = Trash.objects.filter(order_id=order.id, product_id=product.id).last()
        if trash:
            if trash.quantity > 1:
                trash.quantity -= 1
                trash.save()
            else:
                trash.delete()
            order.total_amount = order.get_total_amount()
            order.save()

            self.stdout.write(f'order: {order}\n deleted product: {product}')

        else:
            self.stdout.write(f'object not found')

