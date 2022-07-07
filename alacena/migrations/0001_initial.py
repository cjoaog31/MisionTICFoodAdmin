# Generated by Django 4.0.5 on 2022-07-07 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pantry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('last_modification_date', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima modificacion')),
                ('replenish_Rate', models.IntegerField(choices=[('Q', 'Quincenal'), ('M', 'Mensual')], default='M', verbose_name='Frecuencia de compra')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPantry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name='Ultima modificacion')),
                ('first_update_date', models.DateTimeField(auto_now_add=True, verbose_name='Agregago')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('unit', models.CharField(choices=[('KG', 'Kilogramo'), ('LB', 'Libra'), ('G', 'Gramo'), ('U', 'Unidad'), ('L', 'Litro'), ('ML', 'Mililitro')], default='U', max_length=20, verbose_name='Unidad')),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
                ('pantry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alacena.pantry', verbose_name='Alacena')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alacena.product', verbose_name='Producto')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('active', models.BooleanField(default=True, verbose_name='activa')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
            ],
        ),
        migrations.CreateModel(
            name='WishListProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre producto')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Añadido')),
                ('quantity', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('unit', models.CharField(choices=[('KG', 'Kilogramo'), ('LB', 'Libra'), ('G', 'Gramo'), ('U', 'Unidad'), ('L', 'Litro'), ('ML', 'Mililitro')], default='U', max_length=20, verbose_name='Unidad')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Añadido por')),
                ('pantry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alacena.pantry', verbose_name='Alacena')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingListWishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacena.wishlistproduct', verbose_name='Producto')),
                ('shopping_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacena.shoppinglist', verbose_name='Lista de compras')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingListProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('unit', models.CharField(choices=[('KG', 'Kilogramo'), ('LB', 'Libra'), ('G', 'Gramo'), ('U', 'Unidad'), ('L', 'Litro'), ('ML', 'Mililitro')], default='U', max_length=20, verbose_name='Unidad')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacena.productpantry', verbose_name='Producto')),
                ('shopping_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacena.shoppinglist', verbose_name='Lista de compras')),
            ],
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_date', models.DateTimeField(auto_now_add=True, verbose_name='Añadido')),
                ('read', models.BooleanField(default=True, verbose_name='Activa')),
                ('pantry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alacena.pantry', verbose_name='Alacena')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alacena.product', verbose_name='Producto')),
            ],
        ),
    ]
