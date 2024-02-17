from django.urls import path
from . import views


urlpatterns = [
    path('show_all_products/', views.show_all_products, name='show_all_products'),
    path('edit_prodict/<int:pr_id>/', views.edit_prodict, name='edit_prodict'),
    path('get_orders_by_client_id/<int:client_id>/', views.get_orders_by_client_id, name='get_orders_by_client_id'),
    path('get_products_by_client_id/<int:client_id>/', views.get_products_by_client_id, name='get_products_by_client_id'),

    path('', views.show_all_products, name='show_all_products'),
]
