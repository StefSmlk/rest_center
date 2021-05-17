import datetime
from django import forms
from rooms.models import BookingRoomModel


class DateInput(forms.DateInput):
    input_type = 'date'


class RoomBookForm(forms.ModelForm):
    start = forms.DateField(label='выберите дату заезда', widget=DateInput(format='%d.%m.%Y'))
    end = forms.DateField(label='выберите дату выезда', widget=DateInput(format='%d.%m.%Y'))
    name = BookingRoomModel.name
    room_name = BookingRoomModel.room_name

    class Meta:
        model = BookingRoomModel
        fields = ('start', 'end',)

    def clean(self, *args, **kwargs):
        start = self.cleaned_data['start']
        end = self.cleaned_data['end']
        if start < datetime.date.today():
            raise forms.ValidationError('дата заезда указана неверно')
        if end < start:
            raise forms.ValidationError('дата выезда указана неверно')
        return super().clean(*args, **kwargs)
