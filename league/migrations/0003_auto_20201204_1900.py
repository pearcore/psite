# Generated by Django 2.2.5 on 2020-12-04 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_auto_20201204_1843'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlayerInfo',
            new_name='PlayerLogin',
        ),
    ]