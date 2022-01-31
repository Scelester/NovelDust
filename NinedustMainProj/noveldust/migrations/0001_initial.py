# Generated by Django 3.2.9 on 2021-11-05 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genrelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TopBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topname', models.CharField(max_length=200)),
                ('topcover', models.ImageField(blank=True, null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noveldust.genrelist')),
                ('topbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noveldust.topbooks')),
            ],
        ),
        migrations.CreateModel(
            name='BookItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=None)),
                ('samename', models.BooleanField()),
                ('samecover', models.BooleanField()),
                ('volume_no', models.IntegerField()),
                ('topbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noveldust.topbooks')),
            ],
        ),
    ]
