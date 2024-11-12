from django.db import models

# Create your models here.

class Usuario(models.Model):
    correo = models.EmailField(max_length=100, primary_key=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.correo