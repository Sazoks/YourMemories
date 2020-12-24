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


def add_memories(request):
    """
    Добавление нового воспоминания.
    Если пользователь отослал POST-запрос через форму,
    осуществляем валидацию и сохраняем новые данные.
    """
    if request.method == "POST":
        valid_form = forms.AddMemoriesForm(request.POST)
        if valid_form.is_valid():
            new_place = models.UserPlace()
            new_place.place = valid_form.cleaned_data["place"]
            new_place.header_place = valid_form.cleaned_data["header_place"]
            new_place.description_place = valid_form.cleaned_data["description_place"]
            new_place.save()
    return HttpResponseRedirect("/")


def delete_memories(request, id):
    """
    Удаление воспоминаний.
    Пользователь отсылает GET-запрос с параметром - id воспоминания.
    """
    # Если попытка удаления не увенчалась успехом,
    # сообщаем пользователю, что такой записи нет.
    try:
        models.UserPlace.objects.get(id=id).delete()
        return HttpResponseRedirect("/")
    except models.UserPlace.DoesNotExist:
        return HttpResponseNotFound("<h2>Извините, но забытое однаджы не забудешь дважды.</h2>")
