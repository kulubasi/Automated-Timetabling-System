# Generated by Django 4.1 on 2022-08-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursetitle', models.CharField(max_length=100)),
                ('coursecode', models.CharField(max_length=100)),
                ('lecturer', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=3)),
                ('roomno', models.CharField(max_length=1000)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
            ],
        ),
    ]
