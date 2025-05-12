from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.bashboard, name='dashboard'),
    
    # registro cursos
    path('listar_cursos/', views.listar_cursos, name='listar_cursos'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('editar_curso/<int:id>/', views.editar_curso, name='editar_curso'),
    path('eliminar_curso/<int:id>/', views.eliminar_curso, name='eliminar_curso'),
    
    # registro docentes
    path('listar_docentes/', views.listar_docentes, name='listar_docentes'),
    path('crear_docente/', views.crear_Docente, name='crear_docente'),
    path('editar_docente/<int:id>/', views.editar_Docente, name='editar_docente'),
    path('eliminar_docente/<int:id>/', views.eliminar_Docente, name='eliminar_docente'),
    
    # registro estudiantes
    path('listar_estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('crear_estudiante/', views.crear_Estudiante, name='crear_estudiante'),
    path('editar_estudiante/<int:id>/', views.editar_Estudiante, name='editar_estudiante'),
    path('eliminar_estudiante/<int:id>/', views.eliminar_Estudiante, name='eliminar_estudiante'),
    
    # registro de inscripciones
    path('listar_inscripciones/', views.listar_inscripciones, name='listar_inscripciones'),
    path('crear_inscripcion/', views.crear_Inscripcion, name='crear_inscripcion'),
    path('editar_inscripcion/<int:id>/', views.editar_Inscripcion, name='editar_inscripcion'),
    path('eliminar_inscripcion/<int:id>/', views.eliminar_Inscripcion, name='eliminar_inscripcion'),
    
]
