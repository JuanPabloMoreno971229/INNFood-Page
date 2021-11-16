# Generated by Django 3.2 on 2021-09-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='procedure',
            field=models.CharField(choices=[('P', 'Peticiones'), ('Q', 'Quejas'), ('R', 'Reclamos'), ('S', 'Sugerencias')], max_length=200, null=True, verbose_name='Procedimiento'),
        ),
    ]