from django.shortcuts import render
from django.utils.translation import gettext as _


def get_index(request):
    return render(request, 'index.html', context={})


def get_base(request):
    return render(request, 'base.html', context={})
