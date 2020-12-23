from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserPlace(AbstractBaseUser):
    """
    Модель пользовательской записи.
    Т.к. нам надо знать и хранить информацию от Facebook'a,
    унаследуем класс от AbstractBaseUser.
    """
    place = models.CharField(max_length=200)
    header_place = models.CharField(max_length=50)
    description_place = models.TextField(max_length=200)
