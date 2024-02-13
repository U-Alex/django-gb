from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = "create user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone', type=str, help='User phone')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        client = Client.objects.create(name=kwargs['name'],
                                       email=kwargs['email'],
                                       phone=kwargs['phone'],
                                       address=kwargs['address'],
                                       )
        self.stdout.write(f'client_add: {client}')
