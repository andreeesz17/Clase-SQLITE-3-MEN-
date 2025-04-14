from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True, verbose_name='Correo Electronico')
    
    def __str__(self):
        return f"{self.nombre} - {self.telefono}"