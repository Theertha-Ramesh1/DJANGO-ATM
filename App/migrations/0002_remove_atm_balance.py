# Generated by Django 5.0 on 2023-12-14 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atm',
            name='Balance',
        ),
    ]