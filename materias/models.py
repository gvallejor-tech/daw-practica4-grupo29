from django.db import models
from docentes.models import Docente

class Curso(models.Model):
    nombre = models.CharField(max_length=150, blank=False, null=False)
    creditos = models.PositiveIntegerField(blank=False, null=False)
    nivel = models.CharField(max_length=50, blank=False, null=False)
    horas_semana = models.PositiveIntegerField(blank=False, null=False)
    jornada = models.CharField(max_length=50, blank=False, null=False)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre