from django.shortcuts import render
import logging
# from django.http import HttpResponse, JsonResponse
from random import randint
from typing import Callable
import pandas as pd


# logger = logging.getLogger(__name__)


def custom_log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # logger.info(func.__name__)

        return result
    return wrapper


def heads_or_tails(request, n):
    result = []
    for i in range(n):
        result.append({'попытка': i + 1, 'результат': f"heads_or_tails -> {'heads' if randint(0, 1) else 'tails'}"})

    df = pd.DataFrame(result).to_html()
    return render(request, 'rnd_app/main.html', {'result': df})


def game_cube(request, n):
    result = []
    for i in range(n):
        result.append({'попытка': i + 1, 'результат': f"game_cube -> {randint(1, 6)}"})

    df = pd.DataFrame(result).to_html()
    return render(request, 'rnd_app/main.html', {'result': df})


@custom_log
def rnd_num(request, n):
    result = []
    for i in range(n):
        result.append({'попытка': i + 1, 'результат': f"rnd_num -> {randint(0, 100)}"})

    df = pd.DataFrame(result).to_html()
    return render(request, 'rnd_app/main.html', {'result': df})

