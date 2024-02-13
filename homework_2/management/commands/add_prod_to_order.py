from django.core.management.base import BaseCommand
from ...models import Client, Product, Order, Trash


class Command(BaseCommand):
    help = "add_prod_to_order"

    def add_arguments(self, parser):
        parser.add_argument('cl_id', type=int, help='User ID')
        parser.add_argument('ord_id', type=int, help='Order ID')
        parser.add_argument('prod_id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs['cl_id'])
        order = Order.objects.filter(pk=kwargs['ord_id']).first()
        if not order:
            order = Order.objects.create(client=client, total_amount=0)

        product = Product.objects.get(pk=kwargs['prod_id'])
        trash = Trash.objects.filter(order_id=order.id, product_id=product.id).last()
        if trash:
            trash.quantity += 1
            trash.save()
        else:
            new_trash = Trash(product=product, order=order)
            new_trash.save()
        order.total_amount = order.get_total_amount()
        order.save()

        self.stdout.write(f'order: {order}\nproduct: {product}')
