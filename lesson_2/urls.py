from django.urls import path
from . import views


urlpatterns = [

    path('coin/', views.coin, name='coin'),
    path('coin_statistics/<int:n>/', views.coin_statistics, name='coin_statistics'),
    path('cube/', views.cube, name='cube'),
    path('rnd_num/', views.rnd_num, name='rnd_num'),

]
