# Generated by Django 3.0.2 on 2020-12-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_auto_20201204_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'League',
                'verbose_name_plural': 'Leagues',
            },
        ),
        migrations.AlterModelOptions(
            name='playerlogin',
            options={'verbose_name': 'PlayerLogin', 'verbose_name_plural': 'PlayerLogin'},
        ),
        migrations.AlterModelOptions(
            name='playertoken',
            options={'verbose_name': 'PlayerToken', 'verbose_name_plural': 'PlayerToken'},
        ),
    ]