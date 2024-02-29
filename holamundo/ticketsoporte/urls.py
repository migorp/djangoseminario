
from django.urls import path
from .views import cliente_form, dispositivo_form, incidencia_form, buscar_incidencia, gestion_clientes, actualizar_estado

urlpatterns = [
    path('cliente/', cliente_form, name='cliente_form'),
    path('dispositivo/<int:cliente_id>/', dispositivo_form, name='dispositivo_form'),
    path('incidencia/<int:cliente_id>/<int:dispositivo_id>/', incidencia_form, name='incidencia_form'),
    path('', buscar_incidencia, name='buscar_incidencia'),
    
    #lista incidencias
    path('gestion_clientes/', gestion_clientes, name='gestion_clientes'),
    path('actualizar_estado/<int:incidencia_id>/', actualizar_estado, name='actualizar_estado'),
]