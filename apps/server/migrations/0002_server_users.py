# Generated by Django 3.1.6 on 2021-02-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_servers'),
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='users',
            field=models.ManyToManyField(to='user.User'),
        ),
    ]
