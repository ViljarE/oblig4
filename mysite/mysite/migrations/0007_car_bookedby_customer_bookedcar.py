# Generated by Django 4.0.2 on 2022-11-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_customer_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bookedBy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='bookedCar',
            field=models.IntegerField(default=0),
        ),
    ]
