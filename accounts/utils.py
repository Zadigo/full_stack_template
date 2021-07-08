from django.utils.crypto import get_random_string

def upload_avatar_directory(name, instance):
    name, ext = name.split('.')
    name = get_random_string(length=10)
    return f'avatar/{instance.id}/{name}.{ext}'
