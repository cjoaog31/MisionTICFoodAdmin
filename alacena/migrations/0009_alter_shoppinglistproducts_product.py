# Generated by Django 4.0.5 on 2022-08-02 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alacena', '0008_productpantry_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglistproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacena.product', verbose_name='Producto'),
        ),
    ]
