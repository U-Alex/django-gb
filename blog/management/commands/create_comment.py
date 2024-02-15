from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import randint, choice

from ...models import Author, Post, Comment


class Command(BaseCommand):
    help = "create comment"

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        posts = Post.objects.all()
        for i in range(10):
            comment = Comment(
                author=choice(authors),
                post=choice(posts),
                content="\n".join(lorem_ipsum.paragraphs(7, common=False)),
                date_create=f"2001-03-{randint(10, 30)}",
                date_edit=f"2002-05-{randint(10, 20)}",
            )
            comment.save()

        self.stdout.write(f'create {Comment.objects.count()} comments')
