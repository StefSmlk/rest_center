# Generated by Django 3.1.7 on 2021-04-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski_resort', '0002_bootsrentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='bootsrentmodel',
            name='size',
        ),
        migrations.AddField(
            model_name='bootsrentmodel',
            name='size',
            field=models.ManyToManyField(to='ski_resort.Choices'),
        ),
    ]
