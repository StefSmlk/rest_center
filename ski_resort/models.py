from django.db import models


class BoardRentModel(models.Model):
    name = models.CharField(verbose_name='название', max_length=100)
    photo = models.ImageField(verbose_name='фото', upload_to='images')
    price = models.IntegerField(verbose_name='цена')
    description = models.CharField(verbose_name='описание', max_length=200)

    class Meta:
        verbose_name = 'сноуборд'
        verbose_name_plural = 'сноуборды'


class SkiRentModel(models.Model):
    name = models.CharField(verbose_name='название', max_length=100)
    photo = models.ImageField(verbose_name='фото', upload_to='images')
    price = models.IntegerField(verbose_name='цена')
    description = models.CharField(verbose_name='описание', max_length=200)

    class Meta:
        verbose_name = 'лыжи'
        verbose_name_plural = 'лыжи'


class BootsRentModel(models.Model):
    name = models.CharField(verbose_name='название', max_length=100)
    photo = models.ImageField(verbose_name='фото', upload_to='images')
    price = models.IntegerField(verbose_name='цена')
    description = models.CharField(verbose_name='описание', max_length=200)
    size = models.IntegerField(verbose_name='размер')

    class Meta:
        verbose_name = 'ботинки'
        verbose_name_plural = 'ботинки'