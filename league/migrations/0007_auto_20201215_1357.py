# Generated by Django 3.0.2 on 2020-12-15 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_auto_20201212_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='league_belong',
        ),
        migrations.AddField(
            model_name='club',
            name='league_belong',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='league.League', verbose_name='League to play'),
            preserve_default=False,
        ),
    ]
