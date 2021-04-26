from django.db import models


# Create your models here.
class RoomModel(models.Model):
    name = models.CharField(verbose_name='название', max_length=30)
    description = models.CharField(verbose_name='описание', max_length=150)
    price = models.IntegerField(verbose_name='цена')
    photo = models.ImageField(verbose_name='фото', upload_to='images')

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
