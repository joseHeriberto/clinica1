from django.shortcuts import render, redirect
from .forms import PacienteForm
# api
from rest_framework import generics
from .models import Diagnostico, Paciente, Historia_clinica, Medico, Usuario, Nomina, Insumos, Proveedor, Factura, \
    Servicio
from .serializers import DiagnosticoSerializer, PacienteSerializer, Historia_clinicaSerializer, MedicoSerializer, \
    UsuarioSerializer, NominaSerializer, InsumosSerializer, ProveedorSerializer, FacturaSerializer, ServicioSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
def Home(request):
    return render(request, 'index.html')


def crearPciente(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        if paciente_form.is_valid():
            paciente_form.save()
            return redirect('index')
    else:
        paciente_form = PacienteForm()
        print(paciente_form)
        return render(request, 'estetica/crear_paciente.html', {'paciente_form': paciente_form})


# api
class DiagnosticoList(generics.ListCreateAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class PacienteList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class Historia_clinicaList(generics.ListCreateAPIView):
    queryset = Historia_clinica.objects.all()
    serializer_class = Historia_clinicaSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class MedicoList(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class NominaList(generics.ListCreateAPIView):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class InsumosList(generics.ListCreateAPIView):
    queryset = Insumos.objects.all()
    serializer_class = InsumosSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class ProveedorList(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class FacturaList(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj


class ServicioList(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj
