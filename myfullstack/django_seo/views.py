from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


class PrivacyView(TemplateView):
    template_name = 'privacy.html'

    # @method_decorator(cache_page(60 * 43800))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UseView(TemplateView):
    template_name = 'use.html'

    # @method_decorator(cache_page(60 * 43800))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
