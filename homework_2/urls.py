from django.urls import path
from . import views


urlpatterns = [

    path('get_orders_by_client_id/<int:client_id>/', views.get_orders_by_client_id, name='get_orders_by_client_id'),
    path('get_products_by_client_id/<int:client_id>/', views.get_products_by_client_id, name='get_products_by_client_id'),

]
