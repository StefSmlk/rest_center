# Generated by Django 3.1.7 on 2021-04-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommodel',
            name='photo',
            field=models.ImageField(upload_to='images', verbose_name='фото'),
        ),
    ]