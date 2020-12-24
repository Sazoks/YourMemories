from django import forms


class AddMemoriesForm(forms.Form):
    """Форма для добавления нового воспоминания"""
    place = forms.CharField(max_length=200, widget=forms.HiddenInput)
    header_place = forms.CharField(label="Название", max_length=50)
    description_place = forms.CharField(label="Комментарий", max_length=200)
