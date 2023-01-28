# Generated by Django 3.2.16 on 2023-01-23 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20230122_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gameaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=64, verbose_name='账号数据')),
                ('password', models.CharField(max_length=64, verbose_name='账号密码')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='价格')),
                ('status', models.SmallIntegerField(choices=[(1, '已出售'), (2, '未出售')], default=2, verbose_name='游戏账号状态')),
                ('isban_status', models.SmallIntegerField(choices=[(2, '未封禁状态'), (1, '封禁状态')], default=2, verbose_name='游戏账号封禁状态')),
            ],
        ),
    ]