from django.shortcuts import render
from .models import Author, Post, Comment


def get_posts_by_author(request, author_id):
    posts = Post.objects.filter(author_id=author_id)

    return render(request, 'blog/post.html', {'posts': posts})


def author_post(request, n):
    post = Post.objects.get(pk=n)
    post.count_view += 1
    post.save()
    comments = Comment.objects.filter(post=post)#.order_by('')

    return render(request, 'blog/post.html', {'post': post, 'comments': comments})
