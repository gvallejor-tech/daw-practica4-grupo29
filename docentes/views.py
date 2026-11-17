from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente
from .forms import DocenteForm

def home(request):
    return render(request, 'home.html')

def lista_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes/lista.html', {'docentes': docentes})

def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_docentes')
    else:
        form = DocenteForm()
    return render(request, 'docentes/form.html', {'form': form})

def editar_docente(request, id):
    docente = get_object_or_404(Docente, id=id)
    if request.method == 'POST':
        form = DocenteForm(request.POST, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('lista_docentes')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'docentes/form.html', {'form': form})

def eliminar_docente(request, id):
    docente = get_object_or_404(Docente, id=id)
    if request.method == 'POST':
        docente.delete()
        return redirect('lista_docentes')
    return render(request, 'docentes/eliminar.html', {'docente': docente})

