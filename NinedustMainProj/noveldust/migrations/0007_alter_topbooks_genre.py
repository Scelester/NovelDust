# Generated by Django 3.2.9 on 2021-12-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noveldust', '0006_alter_topbooks_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topbooks',
            name='genre',
            field=models.ManyToManyField(to='noveldust.Genrelist'),
        ),
    ]
