# Generated by Django 3.2.9 on 2022-01-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noveldust', '0017_alter_bookitems_bookfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitems',
            name='bookfile',
            field=models.FileField(null=True, upload_to='media/bookfiles'),
        ),
    ]
