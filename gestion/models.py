from django.db import models
from cuenta.models import Cuenta


# Create your models here.
class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=100, verbose_name = 'Nombre del Cliente')
    idCliente = models.PositiveIntegerField(null = False)
    creationDate = models.DateField(verbose_name="fecha de creacion",auto_now_add=True)
    emailCliente =  models.EmailField(verbose_name="email", max_length=60)
    telefonoCliente = models.CharField(max_length=100, verbose_name = 'Telefono del Cliente', null = True)
    author = models.ForeignKey(Cuenta, default=None, on_delete = models.CASCADE, null= True)


    def __str__(self):
        return self.nombreCliente
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'clientes'
        ordering = ["creationDate"]