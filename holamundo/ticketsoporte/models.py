

from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=50)
    tipocliente = models.CharField(max_length=10, choices=[('hogar', 'Hogar'), ('empresa', 'Empresa')])
    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    tipo = models.CharField(max_length=20, choices=[('portatil', 'Portátil'), ('pc_escritorio', 'PC de escritorio'), ('impresora', 'Impresora'), ('componente', 'Componente'), ('otros', 'Otros')])
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    observacion = models.TextField()
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Incidencia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    descripcion_corta = models.CharField(max_length=100)
    estado_fisico = models.CharField(max_length=80)
    componente_adjunto = models.TextField()
    tipo_servicio = models.CharField(max_length=10, choices=[('remoto', 'Remoto'), ('taller', 'Taller'), ('insitu', 'In Situ')])
    estado = models.CharField(max_length=30, default='no_iniciado', null=True, blank=True, choices=[('no_iniciado', 'No Iniciado'), ('en_proceso', 'En Proceso'), ('confirmacion', 'Esperando Confirmación del Cliente'), ('aprobado_por_cliente', 'Aprobado por el Cliente'), ('finalizado', 'Finalizado'), ('anulado', 'Anulado')])
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    resultado_incidencia = models.TextField(null=True, blank=True)
    sugerencias = models.TextField(null=True, blank=True)

