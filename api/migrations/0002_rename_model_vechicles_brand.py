# Generated by Django 4.2.5 on 2023-10-05 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vechicles',
            old_name='model',
            new_name='brand',
        ),
    ]
