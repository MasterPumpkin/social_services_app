# Generated by Django 5.1.6 on 2025-02-16 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('arrival', 'Arrival'), ('departure', 'Departure')], max_length=10)),
                ('timestamp', models.DateTimeField()),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.visit')),
            ],
        ),
    ]
