# Generated by Django 2.2.4 on 2019-08-23 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190823_0205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contenido',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
    ]
