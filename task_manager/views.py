from django.shortcuts import render


def get_index(request):
    return render(request, 'index.html', context={})


def get_base(request):
    return render(request, 'base.html', context={})
