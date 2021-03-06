# Generated by Django 3.1.7 on 2021-04-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski_resort', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BootsRentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('photo', models.ImageField(upload_to='images', verbose_name='фото')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('description', models.CharField(max_length=200, verbose_name='описание')),
                ('size', models.IntegerField(verbose_name='размер')),
            ],
            options={
                'verbose_name': 'ботинки',
                'verbose_name_plural': 'ботинки',
            },
        ),
    ]
