# Generated by Django 4.2 on 2023-04-28 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asignatura', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignatura',
            old_name='note',
            new_name='grade',
        ),
    ]
