# Generated by Django 2.2.6 on 2019-11-28 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0013_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
