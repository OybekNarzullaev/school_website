# Generated by Django 3.2.6 on 2021-08-13 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_alter_standard_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_id',
        ),
    ]
