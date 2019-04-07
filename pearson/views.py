from django.shortcuts import render, redirect

from pearson.form import PearsonForm
from pearson.models import Pearson


def pearson_home(request):
    data = {"title": "Pearson Operations",
            "pearsons": Pearson.objects.all()}
    return render(request, 'pearson/pearson_home.html', data)


def pearson_form(request):
    form = PearsonForm(request.POST or None)
    data = {"form": form}

    return render(request, 'pearson/form.html', data)


def new(request):
    form = PearsonForm(request.POST or None)

    if form.is_valid():
        form.save()
        return pearson_home(request)

    data = {"form": form}
    return render(request, 'pearson/form.html', data)


def update(request):
    print('b')


def delete(request):
    print('c')


def all(request):
    data = {"pearsons": Pearson.objects.all()}
    return render(request, 'pearson/pearson_home.html', data )
