# Generated by Django 2.2.4 on 2019-08-23 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrada',
            new_name='Post',
        ),
    ]