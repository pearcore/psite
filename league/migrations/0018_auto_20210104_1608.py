# Generated by Django 3.0.2 on 2021-01-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0017_auto_20210104_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_team_kit_color',
            field=models.CharField(default='0000ff', max_length=32),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_kit_color',
            field=models.CharField(default='ff0000', max_length=32),
        ),
        migrations.AlterField(
            model_name='match',
            name='remarks',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='team',
            name='kit1_color',
            field=models.CharField(default='ff0000', max_length=32),
        ),
        migrations.AlterField(
            model_name='team',
            name='kit2_color',
            field=models.CharField(default='0000ff', max_length=32),
        ),
    ]
