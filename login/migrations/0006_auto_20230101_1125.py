# Generated by Django 3.2.16 on 2023-01-01 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_department_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='age',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='department',
            name='data',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
