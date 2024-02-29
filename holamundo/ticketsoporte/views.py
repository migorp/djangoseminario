
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, DispositivoForm, IncidenciaForm, Cliente, Dispositivo


def cliente_form(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            # Redirigir a la vista para crear un dispositivo, pasando el ID del cliente
            return redirect('dispositivo_form', cliente_id=cliente.id)
    else:
        form = ClienteForm()

    return render(request, 'cliente_form.html', {'form': form})

def dispositivo_form(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)

    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            dispositivo = form.save(commit=False)
            dispositivo.cliente = cliente
            dispositivo.save()
            # Redirigir a la vista para crear una incidencia, pasando el ID del cliente y del dispositivo
            return redirect('incidencia_form', cliente_id=cliente.id, dispositivo_id=dispositivo.id)
    else:
        form = DispositivoForm()

    return render(request, 'dispositivo_form.html', {'form': form, 'cliente': cliente})

def incidencia_form(request, cliente_id, dispositivo_id):
    cliente = Cliente.objects.get(id=cliente_id)
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)

    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.cliente = cliente
            incidencia.dispositivo = dispositivo
            incidencia.save()
            # Redirigir a la página de formulario completado u otro destino
            return redirect('cliente_form')
    else:
        form = IncidenciaForm(initial={'cliente': cliente.id, 'dispositivo': dispositivo.id})
        #form = IncidenciaForm()

    return render(request, 'incidencia_form.html', {'form': form, 'cliente': cliente, 'dispositivo': dispositivo})




""" from django.core.mail import send_mail
from django.template.loader import render_to_string

def enviar_correo(cliente, dispositivo, incidencia):
    subject = 'Formulario Completado'
    message = render_to_string('correo_template.txt', {'cliente': cliente, 'dispositivo': dispositivo, 'incidencia': incidencia})
    from_email = 'tu@email.com'
    to_email = [cliente.email]  # Asegúrate de que el modelo Cliente tenga un campo 'email'

    send_mail(subject, message, from_email, to_email) """

# ...
from .models import Incidencia
from .forms import BusquedaIncidenciaForm
from django.http import Http404, HttpResponse

def buscar_incidencia(request):
    incidencia = None

    if request.method == 'POST':
        form = BusquedaIncidenciaForm(request.POST)
        if form.is_valid():
            incidencia_id = form.cleaned_data['incidencia_id']
            try:
                incidencia = Incidencia.objects.get(id=incidencia_id)
            except Incidencia.DoesNotExist:
                raise Http404("La incidencia no existe.")
    else:
        form = BusquedaIncidenciaForm()

    return render(request, 'buscar_incidencia.html', {'form': form, 'incidencia': incidencia})


    

#vista de incidencias
def gestion_clientes(request):
    incidencias = Incidencia.objects.all()
    return render(request, 'gestion_clientes.html', {'incidencias': incidencias})

from .forms import ActualizarEstadoForm

def actualizar_estado(request, incidencia_id):
    incidencia = get_object_or_404(Incidencia, id=incidencia_id)

    if request.method == 'POST':
        form = ActualizarEstadoForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect('gestion_clientes')
    else:
        form = ActualizarEstadoForm(instance=incidencia)

    return render(request, 'actualizar_estado.html', {'form': form})

