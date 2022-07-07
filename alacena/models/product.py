from django.db import models
from authApp.models.user import User

class Product(models.Model):

    name = models.CharField('Nombre', max_length=50)
    creation_date = models.DateTimeField('Fecha de creacion', auto_now_add=True)
    added_by = models.ForeignKey(User,verbose_name='Creador', on_delete= models.DO_NOTHING, null= True)
    

