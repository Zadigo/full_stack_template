from django.apps import apps

def get_userprofile_model():
    from django.conf import settings
    try:
        model = apps.get_model(getattr(settings, 'AUTH_USER_PROFILE_MODEL'))
    except:
        return None
    else:
        return model
