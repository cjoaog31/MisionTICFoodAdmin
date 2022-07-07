from django.db import models
from authApp.models.user import User

class Pantry(models.Model):

    class ReplenishRate(models.TextChoices):
        DIAS15 = 'Q', ('Quincenal')
        DIAS30 = 'M', ('Mensual')

    owner = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE, null= True)
    creation_date = models.DateTimeField("Fecha de creacion", auto_now_add=True)
    last_modification_date = models.DateTimeField("Fecha ultima modificacion", auto_now= True)
    replenish_Rate = models.IntegerField('Frecuencia de compra',choices=ReplenishRate.choices, default= ReplenishRate.DIAS30)
