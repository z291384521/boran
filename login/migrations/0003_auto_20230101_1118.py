# Generated by Django 3.2.16 on 2023-01-01 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_department_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]