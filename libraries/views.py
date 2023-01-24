from django.shortcuts import redirect, render

from .forms import NameForm


def index(request):
    return render(request, '../templates/libraries/index.html')


def add_library(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("library")

    else:
        form = NameForm()

    return render(request, '../templates/libraries/addLibrary.html', {'form': form})
