from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
    help = "get user by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=kwargs['id']).last()
        self.stdout.write(f'client_id {kwargs['id']}: {client}')

