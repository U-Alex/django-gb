from django.urls import path
from . import views


urlpatterns = [

    path('get_posts_by_author/<int:author_id>/', views.get_posts_by_author, name='get_posts_by_author'),
    path('post/<int:n>/', views.author_post, name='author_post'),
    # path('cube/', views.cube, name='cube'),
    # path('rnd_num/', views.rnd_num, name='rnd_num'),

]
