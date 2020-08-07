# Generated by Django 2.2.15 on 2020-08-07 14:57

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('date_pub', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_upd', models.DateField(auto_now=True, verbose_name='date updated')),
                ('status', models.CharField(default='not_validated', max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('category', models.CharField(choices=[('CONS_COND', 'CONSTRUCTION'), ('SPEC_COND', 'SPECIAL_EVENT'), ('INCI_COND', 'INCIDENT'), ('WTHR_COND', 'WEATHER_CONDITION'), ('ROAD_COND', 'ROAD_CONDITION')], max_length=9)),
            ],
        ),
    ]
