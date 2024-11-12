# Django SEO

An application that facilitates SEO and legal template management for a website by passing database content to the Django templates globally.

## How to use

```python
INSTALLED_APPS = [
    'django_seo'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Other context processors...
                'django_analytics.context_processors.legal_business'
                'django_analytics.context_processors.seo'
            ],
            'libraries': {
                # Libraries here
            }
        }
    }
]
```

```html
<html>
    <head>
        <title>{{ seo.linked_in }}</title>
    </head>
</html>
```
