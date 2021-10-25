# Generated by Django 3.1.2 on 2021-10-24 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_celebrities'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='biography',
            field=models.CharField(default='Not Updated Yet', max_length=10000),
        ),
        migrations.AddField(
            model_name='cast',
            name='overview',
            field=models.CharField(default='Not Updated Yet', max_length=1000),
        ),
    ]
