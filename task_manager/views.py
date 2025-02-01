from django.shortcuts import render
from django.views import View

# from django.utils.translation import gettext as _


def get_index(request):
    return render(request, 'index.html', context={})


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', context={})
