from django.shortcuts import render, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta

from .models import Client, Product, Order, Trash


def get_orders_by_client_id(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except ObjectDoesNotExist:
        return HttpResponse('клиент не найден')

    result = {}
    orders = Order.objects.filter(client=client)
    for order in orders:
        trash = Trash.objects.filter(order=order)
        result[order] = trash

    return render(request,
                  'homework_2/show_orders.html',
                  {'client': client, 'result': result}
                  )


def get_products_by_client_id(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except ObjectDoesNotExist:
        return HttpResponse('клиент не найден')

    result = []
    for delta in [7, 30, 365]:
        td = datetime.today() - timedelta(delta)
        result.append(Product.objects.filter(trash__order__client=client, trash__date_add__gt=td).distinct())

    product_count = [q.count() for q in result]

    return render(request,
                  'homework_2/show_products.html',
                  {'client': client, 'result': result, 'product_count': product_count}
                  )
