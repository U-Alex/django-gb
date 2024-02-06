import logging
from random import randint
# from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    logger.info('about page accessed')
    try:
        res = 1 / 0
    except Exception as err:
        logger.exception(f'Error {err}')
    return HttpResponse("About us")


def heads_or_tails(request):
    result = f"heads_or_tails -> {'heads' if randint(0, 1) else 'tails'}"
    logger.info(result)
    return HttpResponse(result)
