# Generated by Django 3.2.16 on 2022-12-20 23:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bnbhouse', '0011_auto_20221220_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='check_in',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]