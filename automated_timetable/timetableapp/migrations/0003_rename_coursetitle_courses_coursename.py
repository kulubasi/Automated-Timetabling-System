# Generated by Django 4.1 on 2022-08-28 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetableapp', '0002_remove_courses_endtime_remove_courses_starttime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='coursetitle',
            new_name='coursename',
        ),
    ]