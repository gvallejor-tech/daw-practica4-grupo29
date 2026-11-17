from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Curso
from .forms import CursoForm

# Create your views here.


# Logica de negocio para crear un nuevo curso
class CrearCursoView(CreateView):
    model = Curso
    template_name = 'materias/crear_curso.html'
    form_class = CursoForm
    success_url = reverse_lazy('listar_cursos')


# Logica de negocio para listar los cursos
class ListarCursoView(ListView):
    model = Curso
    template_name = 'materias/listar_cursos.html'
    context_object_name = 'cursos'
    ordering = ['nombre']


# Logica de negocio para editar un curso
class EditarCursoView(UpdateView):
    model = Curso
    template_name = 'materias/editar_curso.html'
    form_class = CursoForm
    success_url = reverse_lazy('listar_cursos')


# Logica de negocio para eliminar un curso
class EliminarCursoView(DeleteView):
    model = Curso
    template_name = 'materias/eliminar_curso.html'
    context_object_name = 'curso'
    success_url = reverse_lazy('listar_cursos')
