# Generated by Django 4.2.2 on 2023-08-28 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tesapp', '0010_remove_photo_sas_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='name',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='roll_no',
        ),
    ]
