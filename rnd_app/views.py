from django.shortcuts import render
import logging
from django.http import HttpResponse, JsonResponse
from random import randint
from typing import Callable


logger = logging.getLogger(__name__)


def custom_log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(func.__name__)
        print(result)
        return result
    return wrapper


def heads_or_tails(request):
    result = f"heads_or_tails -> {'heads' if randint(0, 1) else 'tails'}"
    logger.info(result)
    return HttpResponse(result)


def game_cube(request):
    result = f"game_cube -> {randint(1, 6)}"
    # logger.info(result)
    return HttpResponse(result)


@custom_log
def rnd_num(request):
    result = f"rnd_num -> {randint(0, 100)}"
    # logger.info(result)
    return JsonResponse({'result': result})




