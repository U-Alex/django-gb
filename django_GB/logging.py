
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': './log/django.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'rnd_app': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'homework_1': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            # 'format': '{levelname} {asctime} {module} {process} {thread} {message}',
            'format': '{levelname} {asctime} {name} {message}',
            'style': '{',
        },
    },
}
