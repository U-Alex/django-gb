from django.contrib import admin

from .models import Author, Post, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'birthdate', 'fullname']
    list_filter = ['birthdate']
    fieldsets = (('основная инф.', {'fields': ['firstname', 'lastname', 'birthdate'],
                                    'description': 'инф. о пользователе',
                                    'classes': ['test_css', 'collapse']}),
                 ('дополнительная инф.', {'fields': ['email', 'bio']}),
                 )
    # actions =
    readonly_fields = ['email', 'birthdate']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'count_view', 'is_public']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'date_create']


