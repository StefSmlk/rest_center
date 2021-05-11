from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class RoomBookForm(forms.Form):
    calendar_start = forms.DateField(label='выберите дату заезда', widget=DateInput())
    calendar_end = forms.DateField(label='выберите дату выезда', widget=DateInput())
