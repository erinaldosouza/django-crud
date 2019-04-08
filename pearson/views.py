from django.shortcuts import render, redirect

from pearson.form import PearsonForm
from pearson.models import Pearson


def home(request):
    data = {"title": "Pearson Operations",
            "pearsons": Pearson.objects.all()}
    return render(request, 'pearson/home.html', data)


def new(request):
    form = PearsonForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('pearsons')

    data = {"form": form}
    return render(request, 'pearson/form.html', data)


def update(request, pk):
    pearson = Pearson.objects.get(pk=pk)
    form = PearsonForm(request.POST or None, instance=pearson)

    if form.is_valid():
        form.save()
        return redirect('pearsons')

    data = {"form": form, "pearson": pearson}
    return render(request, 'pearson/form.html', data)


def delete(request, pk):
    pearson = Pearson.objects.get(pk=pk)
    pearson.delete()
    return redirect('pearsons')

