# Django Analytics

Django analytics is an application that allows the website manager to store all the identifiers for his different analytics tools in a database in order to be used.

## Configuration

Register the template tags in your settings:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Context processors
            ],
            'libraries': {
                'google': 'django_analytics.templatetags.google_analytics',
                'google_ads': 'django_analytics.templatetags.google_ads'
                # Other libraries
            }
        }
    }
]
```

### Google Tag Manager

```html
<html>
    <head>
        {% google_tag_manager %}
    </head>

    <body>
    </body>
</html>
```

### Google Ads and Google Analytics

```html
<html>
    <head>
        {% analytics_and_ads %}
    </head>

    <body>
        {% gtm_no_script %}
    </body>
</html>
```

### Microsoft clarity

```html
<html>
    <head>
        {% microsoft_clarity %}
    </head>

    <body>
    </body>
</html>
```
