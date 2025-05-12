from .models import Docente, Estudiante, Curso, Inscripcion
from django import forms


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
        
        
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
        
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        labels = {
            'usiuario_e': 'Seleccione el usuario',
            'imagen_e': 'seleccione la imagen',
            'matricula': 'agregue la matricula',
          
        }
        
class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        