from django.db import models
from accounts.forms import User


class RoomModel(models.Model):
    name = models.CharField(verbose_name='название', max_length=30)
    description = models.CharField(verbose_name='описание', max_length=150)
    price = models.IntegerField(verbose_name='цена')
    photo = models.ImageField(verbose_name='фото', upload_to='images')

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return self.name


class BookingRoomModel(models.Model):
    start = models.DateField(verbose_name='дата заезда')
    end = models.DateField(verbose_name='дата выезда')
    name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    room_name = models.ForeignKey(RoomModel, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        name_str = f"{self.name} с {self.start.__format__('%d.%m')} по {self.end.__format__('%d.%m')} номер {self.room_name}"
        return name_str
