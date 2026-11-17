from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Docente

# Create your views here.

class prueba(TemplateView):
    template_name = 'docentes/prueba.html'


# Logica de negocio para crear un nuevo docente
class CrearDocenteView(CreateView):
    model = Docente
    template_name = 'docentes/crear_docente.html'
    fields = "__all__"
    success_url = reverse_lazy('listar_docentes')


# Logica de negocio para listar los docentes
class ListarDocenteView(ListView):
    model = Docente
    template_name = 'docentes/listar_docentes.html'
    context_object_name = 'docentes'
    ordering = ['apellido', 'nombre']


# Logica de negocio para editar un docente
class EditarDocenteView(UpdateView):
    model = Docente
    template_name = 'docentes/editar_docente.html'
    fields = "__all__"
    success_url = reverse_lazy('listar_docentes')


# Logica de negocio para eliminar un docente
class EliminarDocenteView(DeleteView):
    model = Docente
    template_name = 'docentes/eliminar_docente.html'
    context_object_name = 'docente'
    success_url = reverse_lazy('listar_docentes')
