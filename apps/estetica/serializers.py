from abc import ABC

from .models import Diagnostico, Paciente, Medico, Insumos, Historia_clinica, Proveedor, Factura, Usuario, Servicio, \
    Nomina
from rest_framework import serializers


class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ('Codigo_cups', 'Abreviatura', 'Nombre', 'Descripcion')


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('Identificacion_paciente', 'Nombre', 'PrimerApellido', 'SegundoApellido', 'Fecha_nacimiento', 'Sexo',
                  'estado_civil', 'Ocupacion',
                  'Email', 'Telefeno', 'Residencia', 'Ciudad', 'Departamento')


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('Identificacion_medico', 'Nombre', 'PrimerApellido', 'SegundoApellido', 'Sexo',
                  'Email', 'Telefeno', 'Residencia', 'Ciudad', 'Departamento')


class Historia_clinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia_clinica
        fields = ('Identificacion_historia', 'Paciente_Nombre', 'Fecha_inicio', 'Fecha_fin', 'Motivo_consulta',
                  'Consecutivo', 'Id_Medico', 'Diagnostico_codigo', 'Servicio', 'Anexo', 'Antecedentes')


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('Codigo_cups', 'Abreviatura', 'Nombre', 'Descripcion')


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('Identificacion_factura', 'Fact_hisCllin', 'Detalle', 'Cantidad', 'Valor',
                  'Iva', 'Fecha_factura', 'Subtotal', 'Total')


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('Identificacion_proveedor', 'Nombre', 'Ciudad', 'Departamento', 'Producto', 'Cantidad')


class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumos
        fields = ('Identificacion_insumo', 'Nombre', 'Cantidad', 'Cantidad_salida', 'Existencia', 'Fecha_ingreso',
                  'Fecha_vencimiento', 'Id_Proveedor')


class NominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomina
        fields = ('Identificacion_nomina', 'Fecha_inicio', 'Fecha_fin', 'Detalle', 'Identificacion_especialista')


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('Identificacion_usario', 'Usuario', 'Email', 'Rol', 'Password')
