# Generated by Django 4.0.5 on 2022-07-25 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alacena', '0005_userpantrypermission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpantry',
            name='quantity',
            field=models.FloatField(verbose_name='Cantidad'),
        ),
    ]