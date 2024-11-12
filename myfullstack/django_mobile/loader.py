from django.template.engine import Engine
from django.conf import settings
from django.template.loaders.base import Loader
from django.template.exceptions import TemplateDoesNotExist
from django.template.loaders.cached import Loader as CachedLoader


class DjangoMobileTemplateLoader(Loader):
    @staticmethod
    def _refix_template_name(name):
        """We want to load templates 
        from `mobile/template.html` 
        whichever the app"""
        return f'mobile/{name}'

    @staticmethod
    def _template_loaders(self):
        loaders = []
        django_mobile_template_loaders = getattr(
            settings, 'DJANGO_MOBILE_TEMPLATE_LOADERS', [])
        engine = Engine.get_default()
        for loader_path in django_mobile_template_loaders:
            loader = engine.find_template_loader(loader_path)
            if not loader:
                continue
            loaders.append(loader)
        return loaders

    def get_template_sources(self, template_name):
        template_name = self._refix_template_name(template_name)
        for loader in self._template_loaders:
            try:
                return loader.load_template_source(template_name)
            except Exception:
                raise TemplateDoesNotExist('Mobile template does '
                                           f'not exist. Tried: {template_name}')


class DjangoMobileCachedTemplateLoader(CachedLoader):
    def cache_key(self, template_name, skip=[]):
        return f'mobile:{template_name}'
