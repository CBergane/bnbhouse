# Generated by Django 3.2.16 on 2022-12-16 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bnbhouse', '0004_auto_20221215_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='guest',
            new_name='user',
        ),
    ]
