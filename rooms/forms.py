from django import forms
from django.contrib.admin import widgets

from rooms.models import RoomModel


class RoomBookForm(forms.Form):
    calendar_start = forms.DateField(label='выберите дату заезда', widget=forms.SelectDateWidget())
    calendar_end = forms.DateField(label='выберите дату выезда', widget=forms.SelectDateWidget())
