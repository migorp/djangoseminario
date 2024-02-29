

from django import forms
from .models import Cliente, Dispositivo, Incidencia

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = '__all__'
        widgets = {
            'cliente': forms.HiddenInput(),  # Este widget ocultará el campo en el formulario HTML
        }
        def __init__(self, *args, **kwargs):
            super(DispositivoForm, self).__init__(*args, **kwargs)
            self.fields['cliente'].required = False

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(IncidenciaForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['disabled'] = 'disabled'
        self.fields['dispositivo'].widget.attrs['disabled'] = 'disabled'
        self.fields['estado'].widget.attrs['disabled'] = 'disabled'
        self.fields['costo'].widget = forms.HiddenInput()
        self.fields['resultado_incidencia'].widget = forms.HiddenInput()
        self.fields['sugerencias'].widget = forms.HiddenInput()





class BusquedaIncidenciaForm(forms.Form):
    incidencia_id = forms.IntegerField(label='ID de Incidencia', min_value=1)



#lista incidencias
class ActualizarEstadoForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['estado', 'descripcion_corta', 'estado_fisico', 'costo', 'resultado_incidencia', 'sugerencias']