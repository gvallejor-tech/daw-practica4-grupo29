from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Docente
from .forms import DocenteForm


class CrearDocenteView(CreateView):
    model = Docente
    form_class = DocenteForm
    success_url = '/docentes/'
    template_name = 'docentes/form.html'


class ListarDocenteView(ListView):
    model = Docente
    template_name = 'docentes/lista.html'
    context_object_name = 'docentes'


class EditarDocenteView(UpdateView):
    model = Docente
    form_class = DocenteForm
    success_url = '/docentes/'
    template_name = 'docentes/form.html'


class EliminarDocenteView(DeleteView):
    model = Docente
    success_url = '/docentes/'
    template_name = 'docentes/eliminar.html'


