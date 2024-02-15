from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import randint, choice

from ...models import Author


class Command(BaseCommand):
    help = "create authors"

    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(
                firstname=f"fName_{i+1}",
                lastname=f"lName_{i+1}",
                email=f"user_{i+1}@mail.com",
                bio=" ".join(lorem_ipsum.paragraphs(5)),
                birthdate=f"{choice(range(1978, 2020))}-01-{randint(1, 28)}",
            )
            author.fullname = author.get_fullname()
            author.save()

        self.stdout.write(f'create {Author.objects.count()} authors')
