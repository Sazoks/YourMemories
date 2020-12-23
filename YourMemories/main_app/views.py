from . import forms
from . import models
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    """Страница входа"""
    return render(request, 'login.html')


@login_required
def home(request):
    """
    Домашняя страница.
    Если пользователь авторизировался, отправляем ему список
    воспоминаний и форму для создания новых воспоминаний.
    """
    data = {
        "list_places": models.UserPlace.objects.all(),
        "form_memories": forms.AddMemoriesForm(),
    }
    return render(request, 'home.html', context=data)
