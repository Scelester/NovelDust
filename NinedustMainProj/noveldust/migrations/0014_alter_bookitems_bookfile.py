# Generated by Django 3.2.9 on 2022-01-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noveldust', '0013_alter_bookitems_bookfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitems',
            name='bookfile',
            field=models.FileField(null=True, upload_to='media/bookfiles/<property object at 0x000001F7B409F4F0>'),
        ),
    ]
