# Generated by Django 3.0.2 on 2020-01-07 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='简询名称')),
                ('CreateDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('stResult', models.CharField(default='', max_length=200, verbose_name='字符串应答')),
                ('itResult', models.IntegerField(default=0, verbose_name='整型应答')),
                ('jsResult', models.TextField(default='', verbose_name='json应答')),
            ],
            options={
                'verbose_name': '网上简询',
                'verbose_name_plural': '网上简询',
            },
        ),
    ]
