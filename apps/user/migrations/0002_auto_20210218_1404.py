# Generated by Django 3.1.6 on 2021-02-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='server',
        ),
        migrations.AddField(
            model_name='user',
            name='servers',
            field=models.ManyToManyField(to='server.Server'),
        ),
    ]
