from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import randint, choice

from ...models import Author, Post


class Command(BaseCommand):
    help = "create post"

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        for i in range(10):
            post = Post(
                author=choice(authors),
                title=lorem_ipsum.words(5, common=False),
                content="\n".join(lorem_ipsum.paragraphs(7, common=False)),
                date_pub=f"2001-03-{randint(10, 30)}",
                category=choice(lorem_ipsum.WORDS).capitalize(),
            )
            post.save()

        self.stdout.write(f'create {Post.objects.count()} posts')
