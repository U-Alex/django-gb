from django.core.management.base import BaseCommand
from ...models import Author, Post, Comment


class Command(BaseCommand):
    help = "get_posts_by_author"

    def add_arguments(self, parser):
        parser.add_argument('author_name', type=str, help='author_name')

    def handle(self, *args, **kwargs):
        posts = Post.objects.filter(author__fullname__icontains=kwargs['author_name'])

        self.stdout.write(f"{posts}")



