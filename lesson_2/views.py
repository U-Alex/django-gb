from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from random import randint, choice

from .models import Coin


def coin(request):
    result = choice(["орел", "решка"])
    Coin.objects.create(side=result)
    return HttpResponse(result)


def coin_statistics(request, n):
    return JsonResponse(Coin.get_last_n_flip(n), json_dumps_params={'ensure_ascii': False})


def cube(request):
    result = f"cube -> {randint(1, 6)}"
    return HttpResponse(result)


def rnd_num(request):
    result = f"rnd_num -> {randint(0, 100)}"
    return JsonResponse({'result': result})





