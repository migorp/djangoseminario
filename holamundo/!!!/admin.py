from django.contrib import admin
from .models import Cliente, Dispositivo, Incidencia

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','identificacion', 'nombre', 'telefono', 'ciudad', 'tipocliente')
    search_fields = ('nombre', 'identificacion')

admin.site.register(Cliente, ClienteAdmin)

class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('id','tipo', 'marca', 'modelo', 'serie', 'observacion')
    search_fields = ('marca', 'modelo', 'serie')

admin.site.register(Dispositivo, DispositivoAdmin)

class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('id','cliente', 'dispositivo', 'fecha_registro', 'descripcion_corta', 'estado')
    search_fields = ('cliente__nombre', 'dispositivo__marca', 'descripcion_corta')
    list_filter = ('estado', 'tipo_servicio')

admin.site.register(Incidencia, IncidenciaAdmin)