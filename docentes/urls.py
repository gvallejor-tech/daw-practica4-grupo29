from django.urls import path
from .views import home, ListarDocenteView, CrearDocenteView, EditarDocenteView, EliminarDocenteView

urlpatterns = [
    path('', home, name='home'),
    path('docentes/', ListarDocenteView.as_view(), name='lista_docentes'),
    path('docentes/crear/', CrearDocenteView.as_view(), name='crear_docente'),
    path('docentes/editar/<int:pk>/', EditarDocenteView.as_view(), name='editar_docente'),
    path('docentes/eliminar/<int:pk>/', EliminarDocenteView.as_view(), name='eliminar_docente'),
]

