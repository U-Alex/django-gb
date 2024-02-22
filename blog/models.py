from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthdate = models.DateField()
    fullname = models.CharField(max_length=200)

    def get_fullname(self):
        return f"{self.firstname} {self.lastname} {self.fullname}"

    def save(self, *args, **kwargs):
        self.fullname = f"{self.firstname} {self.lastname}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fullname}"


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_pub = models.DateField()
    category = models.CharField(max_length=100)
    count_view = models.IntegerField(default=0)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} | {self.title}"


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_create = models.DateField()
    date_edit = models.DateField()

