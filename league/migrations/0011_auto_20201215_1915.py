# Generated by Django 3.0.2 on 2020-12-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0010_auto_20201215_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(default=[], null=True, to='league.PlayerLogin'),
        ),
    ]
