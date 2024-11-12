def get_admin_site():
    """If the user has created a custom admin, the
    Analytics database will not apprear in the latter.
    Use this function to return the custom or default
    admin based on configuration"""
    from django.conf import settings
    from django.utils.module_loading import import_string
    custom_admin = getattr(settings, 'ADMIN_SITE', None)
    if custom_admin is None:
        from django.contrib.admin.sites import site
        return site
    try:
        module = import_string(custom_admin)
    except:
        raise ImportError(
            "Could not get the module for the custom admin parameter")
    else:
        custom_admin_site_variable = getattr(module, 'custom_admin_site', None)
        if custom_admin_site_variable is None:
            raise ValueError("Module needs to specify a 'custom_admin_site'")
        return custom_admin_site_variable
