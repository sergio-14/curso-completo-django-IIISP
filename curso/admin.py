from django.contrib import admin

from .models import Docente, Estudiante, Curso, Inscripcion

# Register your models here.

admin.site.register(Docente)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Inscripcion)
