from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('docentes/', views.lista_docentes, name='lista_docentes'),
    path('docentes/crear/', views.crear_docente, name='crear_docente'),
    path('docentes/editar/<int:id>/', views.editar_docente, name='editar_docente'),
    path('docentes/eliminar/<int:id>/', views.eliminar_docente, name='eliminar_docente'),
]
