from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['Identificacion_paciente', 'Nombre', 'PrimerApellido', 'SegundoApellido', 'Fecha_nacimiento', 'Sexo',
                  'estado_civil', 'Ocupacion', 'Email', 'Telefeno', 'Residencia', 'Ciudad', 'Departamento']
