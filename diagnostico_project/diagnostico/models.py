from django.db import models

class Diagnostico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=2, choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extranjería')])
    numero_documento = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    peso = models.IntegerField()
    fuma = models.CharField(max_length=2, choices=[('si', 'Sí'), ('no', 'No')])
    sexo = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')])
    estatura = models.IntegerField()
    antecedentes_medicos = models.TextField()
    sintomas_generales = models.TextField()
    enfermedad_predicha = models.CharField(max_length=100)
    fecha_diagnostico = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.enfermedad_predicha}"
