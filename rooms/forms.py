from django import forms

from rooms.models import BookingRoomModel


class DateInput(forms.DateInput):
    input_type = 'date'


class RoomBookForm(forms.ModelForm):
    start = forms.DateField(label='выберите дату заезда', widget=DateInput(format='%d.%m.%Y'))
    end = forms.DateField(label='выберите дату выезда', widget=DateInput(format='%d.%m.%Y'))
    name = BookingRoomModel.name

    class Meta:
        model = BookingRoomModel
        fields = ('start', 'end',)

    # def clean_calendar_start(self):
    #     calendar_start = self.cleaned_data['calendar_start']
    #     print(calendar_start)
    #     print(datetime.date.today())
    #     if calendar_start < datetime.date.today():
    #         raise forms.ValidationError('дата указана неверно')
    #     return calendar_start
    #
    # def clean_calendar_end(self):
    #     calendar_end = self.cleaned_data['calendar_end']
    #     calendar_start = RoomBookForm.clean_calendar_start(self)
    #     if calendar_end < calendar_start:
    #         raise forms.ValidationError('дата указана неверно')
    #     return calendar_end


