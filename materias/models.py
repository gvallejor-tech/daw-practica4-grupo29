from django.db import models
from docentes.models import Docente

class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    creditos = models.PositiveIntegerField()
    nivel = models.CharField(max_length=50)
    horas_semana = models.PositiveIntegerField()
    jornada = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre