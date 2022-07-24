from django.db import models
from authApp.models.user import User


class ReplenishRate(models.TextChoices):
    DIAS15 = 'Q', ('Quincenal')
    DIAS30 = 'M', ('Mensual')

class Pantry(models.Model):

    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE, null= True)
    creation_date = models.DateTimeField("Fecha de creacion", auto_now_add=True)
    last_modification_date = models.DateTimeField("Fecha ultima modificacion", auto_now= True)
    replenish_rate = models.CharField('Frecuencia de compra',choices=ReplenishRate.choices, default= ReplenishRate.DIAS30, max_length=1)
