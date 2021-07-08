from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control


def index(request):
    return render(request, template_name='index.html')
