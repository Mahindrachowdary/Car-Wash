# Generated by Django 4.0 on 2022-11-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_remove_booking_count_booking_place_booking_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='approval',
            field=models.CharField(choices=[('S', 'Success'), ('P', 'Pending'), ('R', 'Rejected')], default='P', max_length=250),
        ),
    ]
