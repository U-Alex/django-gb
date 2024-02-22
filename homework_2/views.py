from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta

from .models import Client, Product, Order, Basket
from .forms import EditProductForm


def show_all_products(request):
    return render(request,
                  'homework_2/show_all_products.html',
                  {'products': Product.objects.all()}
                  )


def edit_prodict(request, pr_id: int = 0):
    try:
        product = Product.objects.get(pk=pr_id) if pr_id else 0
    except ObjectDoesNotExist:
        return HttpResponse('товар не найден')

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product) \
            if pr_id \
            else EditProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../../show_all_products')
    else:
        form = EditProductForm(instance=product) \
            if pr_id \
            else EditProductForm()

    return render(request,
                  'homework_2/edit_product.html',
                  {'form': form, 'product': product}
                  )


def get_orders_by_client_id(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except ObjectDoesNotExist:
        return HttpResponse('клиент не найден')

    result = {}
    orders = Order.objects.filter(client=client)
    for order in orders:
        trash = Basket.objects.filter(order=order)
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
