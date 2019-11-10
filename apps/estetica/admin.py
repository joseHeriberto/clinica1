from django.contrib import admin

from .models import Diagnostico,Usuario,Servicio,Factura,Historia_clinica,Insumos,Medico,Nomina,Paciente,Proveedor
from django.contrib import admin
from django.contrib.auth.models import Group, User

admin.site.site_header = 'Clinica'

admin.site.register(Diagnostico)
admin.site.register(Factura)
admin.site.register(Historia_clinica)
admin.site.register(Insumos)
admin.site.register(Medico)
admin.site.register(Nomina)
admin.site.register(Paciente)
admin.site.register(Proveedor)
admin.site.register(Servicio)
admin.site.register(Usuario)



admin.site.unregister(User)
admin.site.unregister(Group)