from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# @method_decorator(cache_page(10 * 60), name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'
