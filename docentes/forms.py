from django import forms
from .models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'correo', 'cedula', 'tipo_sangre', 'direccion', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_sangre': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

