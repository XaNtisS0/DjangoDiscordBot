# Generated by Django 3.1.6 on 2021-02-19 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210218_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='servers',
        ),
    ]