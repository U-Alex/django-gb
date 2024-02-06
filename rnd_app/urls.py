from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    # path('about/', views.about, name='about'),

    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('game_cube/', views.game_cube, name='game_cube'),
    path('rnd_num/', views.rnd_num, name='rnd_num'),

]
