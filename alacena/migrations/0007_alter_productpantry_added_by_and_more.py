# Generated by Django 4.0.5 on 2022-07-25 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alacena', '0006_alter_productpantry_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpantry',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Creador'),
        ),
        migrations.AlterField(
            model_name='productpantry',
            name='pantry',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='alacena.pantry', verbose_name='Alacena'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productpantry',
            name='product',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='alacena.product', verbose_name='Producto'),
            preserve_default=False,
        ),
    ]