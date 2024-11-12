# Django mobile

Django mobile checks whether the incoming request comes from a mobile phone and implements on both the request in the template context the result of the test.

## How to use

```python
INSTALLED_APPS = [
    ...
    'django_mobile'
]

```

```python
MIDDLEWARE = [
    ...
    'django_mobile.middleware.DjangoMobileMiddleware'
]

```

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...
                'django_mobile.context_processors.is_mobile'
            ],
            'libraries': {}
        },
    },
]
```

