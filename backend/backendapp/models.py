from django.db import models

# Create your models here.

class Ticket(models.Model):
    fecha_inicio = models.DateField(blank=True, null=True)  # Permitir que el campo esté en blanco y sea nulo
    fecha_fin = models.DateField(blank=True, null=True)  # Permitir que el campo esté en blanco y sea nulo
    simbolo = models.CharField(max_length=50, default='IBM', choices=[('IBM', 'IBM'), ('APPL', 'APPL'), ('TSLA', 'TSLA')]) # Longitud máxima del campo, valor predeterminado y opciones posibles

class RequestLog(models.Model):
    url = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class DatosFinancieros(models.Model):
    fecha = models.DateField()
    apertura = models.FloatField()
    maximo = models.FloatField()
    minimo = models.FloatField()
    cierre = models.FloatField()
    adj_close = models.FloatField()
    volumen = models.IntegerField()

    # Otros campos según tus necesidades

    def __str__(self):
        return str(self.fecha)