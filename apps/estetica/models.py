from django.db import models

class Diagnostico(models.Model):
    Codigo_cups=models.IntegerField(blank=False, null=False, verbose_name='Codígo')
    Abreviatura= models.CharField(max_length=200, blank=False, null=False, verbose_name='Abreviatura')
    Nombre=models.CharField(max_length=200, blank=False, null=False, verbose_name='Nombre')
    Descripcion= models.TextField(max_length=200, blank=False, null=False, verbose_name='Descripción')

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ['Nombre']
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'


class Paciente(models.Model):
    Identificacion_paciente= models.IntegerField(primary_key=True, verbose_name='Identificación')
    Nombre = models.CharField(max_length=200, blank=False, verbose_name='Nombre')
    PrimerApellido = models.CharField(max_length=200, blank=False, verbose_name='Primer apellido')
    SegundoApellido=models.CharField(max_length=200, blank=False, verbose_name='Segundo apellido')
    Fecha_nacimiento= models.DateField(max_length=200, blank=False, verbose_name='Nacimiento')
    Sexo= models.CharField(max_length=200, blank=False, verbose_name='Sexo')
    estado_civil= models.CharField(max_length=200, blank=True, null=True, verbose_name='Estado civil')
    Ocupacion = models.CharField(max_length=200, blank=False, verbose_name='Ocupación')
    Email= models.EmailField(max_length=200, blank=False, verbose_name='Email')
    Telefeno =models.CharField(max_length=200, blank=False, verbose_name='Teléfono')
    Residencia = models.CharField(max_length=200, blank=False, verbose_name='Residencia')
    Ciudad = models.CharField(max_length=200, blank=False, verbose_name='Ciudad')
    Departamento = models.CharField(max_length=200, blank=False, verbose_name='Depatamento')

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering =['Nombre']
        verbose_name='Paciente'
        verbose_name_plural ='Pacientes'

class Medico(models.Model):
    Identificacion_medico= models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nombre')
    PrimerApellido = models.CharField(max_length=200, blank=False, null=False, verbose_name='Primer apellido')
    SegundoApellido=models.CharField(max_length=200, blank=False, null=False, verbose_name='Segundo apellido')
    Sexo= models.CharField(max_length=200, blank=False, null=False, verbose_name='Genero')
    Email= models.EmailField(max_length=200, blank=False, null=False, verbose_name='Email')
    Telefeno =models.IntegerField(blank=False, null=False, verbose_name='Teléfono')
    Residencia = models.CharField(max_length=200, blank=False, null=False, verbose_name='Residencia')
    Ciudad=models.TextField(max_length=200, blank=False, null=False, verbose_name='Ciudad')
    Departamento=models.TextField(max_length=200, blank=False, null=False, verbose_name='Departamento')

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ['Nombre']
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

class Historia_clinica(models.Model):
    Identificacion_historia= models.IntegerField(primary_key=True)
    Paciente_Nombre = models.OneToOneField(Paciente, on_delete=models.CASCADE, null=True)
    Fecha_inicio = models.DateField(max_length=200, blank=False, null=False, verbose_name='Fecha de inicio')
    Fecha_fin = models.DateField(max_length=200, blank=False, null=False, verbose_name='Fecha fin')
    Motivo_consulta = models.TextField(max_length=200, blank=False, null=False, verbose_name='Motivo de consulta')
    Consecutivo=models.IntegerField(null=False, verbose_name='Consecutivo')
    Id_Medico=models.ManyToManyField(Medico, verbose_name='Medico')
    Diagnostico_codigo= models.ManyToManyField(Diagnostico,  verbose_name='Diagnostico')
    Servicio= models.TextField(max_length=200, blank=False, null=False, verbose_name='Servicio')
    Anexo= models.TextField(max_length=200, blank=False, null=False, verbose_name='Anexo')
    Antecedentes= models.TextField(max_length=200, blank=False, null=True, verbose_name='Antecedentes')




    def __str__(self):
        return self.Servicio

    class Meta:
        ordering = ['Servicio']
        verbose_name = 'Historia'
        verbose_name_plural = 'Historias'


class Servicio(models.Model):
    Codigo_cups=models.IntegerField(blank=False, null=False, verbose_name='Codígo')
    Abreviatura= models.CharField(max_length=200, blank=False, null=False, verbose_name='Abreviatura')
    Nombre=models.CharField(max_length=200, blank=False, null=False, verbose_name='Nombre')
    Descripcion= models.TextField(max_length=200, blank=False, null=False, verbose_name='Descripción')

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ['Nombre']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

class Factura(models.Model):
            Identificacion_factura = models.AutoField(primary_key=True)
            Fact_hisCllin = models.OneToOneField(Historia_clinica, on_delete=models.CASCADE, null=True, verbose_name='Historia Clínica')
            Detalle = models.ManyToManyField(Servicio, verbose_name='Detalle')
            Cantidad = models.IntegerField(blank=False, null=False, verbose_name='Cantidad')
            Valor = models.IntegerField(blank=False, null=False, verbose_name='Valor')
            Iva = models.IntegerField(blank=False, null=False, verbose_name='Iva')
            Fecha_factura = models.DateTimeField(blank=False, null=True, verbose_name='Fecha')
            Subtotal = models.IntegerField(blank=False, null=False, verbose_name='Subtotal')
            Total = models.IntegerField(blank=False, null=False, verbose_name='Total')

            def __int__(self):
                return self.Cantidad

            class Meta:
                ordering = ['Cantidad']
                verbose_name = 'Factura'
                verbose_name_plural = 'Facturas'


class Proveedor(models.Model):
    Identificacion_proveedor= models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200, blank=False, verbose_name='Nombre')
    Ciudad = models.CharField(max_length=200, blank=False, verbose_name='Ciudad')
    Departamento=models.CharField(max_length=200, blank=False, verbose_name='Departamento')
    Producto= models.CharField(max_length=200, blank=False, verbose_name='Producto')
    Cantidad= models.IntegerField(blank=False, verbose_name='Cantidad')

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ['Nombre']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class Insumos(models.Model):
    Identificacion_insumo= models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nombre')
    Cantidad = models.IntegerField(blank=False, null=False, verbose_name='Cantidad')
    Cantidad_salida=models.IntegerField(blank=False, null=False, verbose_name='Cantidad de salida')
    Existencia= models.IntegerField(blank=False, null=False, verbose_name='Existencia')
    Fecha_ingreso= models.DateTimeField(max_length=200, blank=False, null=False, verbose_name='Fecha de ingreso')
    Fecha_vencimiento= models.DateTimeField(max_length=200, null=True, verbose_name='Fecha de caducidad')
    Id_Proveedor= models.ManyToManyField(Proveedor, verbose_name='Proveedor')

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ['Nombre']
        verbose_name = 'Isumo'
        verbose_name_plural = 'Insumos'

class Nomina(models.Model):
    Identificacion_nomina= models.AutoField(primary_key=True)
    Fecha_inicio = models.DateTimeField(blank=False, null=False, verbose_name='Fecha inicio')
    Fecha_fin= models.DateTimeField(blank=False, null=False, verbose_name='Fecha fin')
    Detalle=models.TextField(blank=False, null=False, verbose_name='Detalle')
    Identificacion_especialista= models.OneToOneField(Medico, on_delete=models.CASCADE, verbose_name='Identificación Medico')

    def __str__(self):
        return self.Detalle

    class Meta:
        ordering = ['Detalle']
        verbose_name = 'Nomina'
        verbose_name_plural = 'Nominas'

class Usuario(models.Model):
    Identificacion_usario= models.AutoField(primary_key=True)
    Usuario = models.CharField(max_length=200, blank=False, null=False, verbose_name='Usuario')
    Email = models.EmailField(max_length=200, blank=False, null=False, verbose_name='Email')
    Rol = models.CharField(max_length=200, blank=False, null=False, verbose_name='Rol')
    Password = models.CharField(max_length=200, blank=False, null=False, verbose_name='Contraseña')

    def __str__(self):
        return self.Usuario

    class Meta:
        ordering = ['Usuario']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'




