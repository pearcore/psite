# Generated by Django 3.0.2 on 2020-02-02 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20200202_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usergroup',
            options={'verbose_name': '用户分组', 'verbose_name_plural': '用户分组s'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户详情', 'verbose_name_plural': '用户详情s'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name': '用户角色', 'verbose_name_plural': '用户角色s'},
        ),
        migrations.AlterModelOptions(
            name='usertoken',
            options={'verbose_name': '用户token', 'verbose_name_plural': '用户token'},
        ),
    ]
