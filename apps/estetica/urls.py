from django.urls import path
from .views import crearPciente, DiagnosticoList

#api
from django.conf.urls import url
from apps.estetica.views import *


urlpatterns =[
    path('crear_paciente/',crearPciente, name='crear_paciente'),
#api
    path('diagnostico/', DiagnosticoList.as_view(), name='diagnostico'),
    path('Paciente/', PacienteList.as_view(), name='Paciente'),
    path('Historiacli/', Historia_clinicaList.as_view(), name='Historiacli'),
    path('Medico/', MedicoList.as_view(), name='Medico'),
    path('Usuario/', UsuarioList.as_view(), name='Usuario'),
    path('Nomina/', NominaList.as_view(), name='Nomina'),
    path('Insumos/', InsumosList.as_view(), name='Insumos'),
    path('Proveedor/', ProveedorList.as_view(), name='Proveedor'),
    path('Factura/', FacturaList.as_view(), name='Factura'),
    path('Servicio/', ServicioList.as_view(), name='Servicio'),

]

