# Generated by Django 3.2 on 2021-10-07 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210924_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitas',
            name='fecha',
            field=models.CharField(default='', max_length=10),
        ),
    ]