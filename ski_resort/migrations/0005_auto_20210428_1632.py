# Generated by Django 3.1.7 on 2021-04-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski_resort', '0004_auto_20210428_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='size',
            field=models.IntegerField(verbose_name='размер'),
        ),
    ]