# Generated by Django 3.2.9 on 2021-12-22 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noveldust', '0005_auto_20211222_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topbooks',
            name='genre',
            field=models.ManyToManyField(blank=True, to='noveldust.Genrelist'),
        ),
    ]