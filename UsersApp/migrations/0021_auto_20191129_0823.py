# Generated by Django 2.2.6 on 2019-11-29 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0020_auto_20191129_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='bookingid',
            field=models.UUIDField(default='62c869387f', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]