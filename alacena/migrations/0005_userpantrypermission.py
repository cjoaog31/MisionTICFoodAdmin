# Generated by Django 4.0.5 on 2022-07-23 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alacena', '0004_productpantry_expiration_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPantryPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de adicion')),
                ('last_modification_date', models.DateTimeField(auto_now=True, verbose_name='Fecha ultima modificacion')),
                ('profile', models.CharField(choices=[('F', 'Familia'), ('I', 'Invitado')], default='I', max_length=1, verbose_name='Perfil')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('pantry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alacena.pantry', verbose_name='Alacena')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
