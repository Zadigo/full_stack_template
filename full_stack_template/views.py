from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control

# @cache_control(max_age=3600)
def index(request):
    return render(request, template_name='index.html', context={})


def redirect_view(request):
    return redirect('/')
