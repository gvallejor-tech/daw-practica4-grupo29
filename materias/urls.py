from django.urls import path
from .views import CrearCursoView, ListarCursoView, EditarCursoView, EliminarCursoView

urlpatterns = [
    path('addCurso/', CrearCursoView.as_view(), name='agregar_curso'),
    path('listCursos/', ListarCursoView.as_view(), name='listar_cursos'),
    path('editCurso/<int:pk>/', EditarCursoView.as_view(), name='editar_curso'),
    path('deleteCurso/<int:pk>/', EliminarCursoView.as_view(), name='eliminar_curso'),
]
