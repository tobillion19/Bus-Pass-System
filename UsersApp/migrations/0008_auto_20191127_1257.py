# Generated by Django 2.2.6 on 2019-11-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0007_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
