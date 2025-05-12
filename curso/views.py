from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Docente, Estudiante, Inscripcion
from .forms import CursoForm, DocenteForm, EstudianteForm, InscripcionForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def bashboard(request):
    return render(request, 'dashboard.html')


#registro de cursos
def listar_cursos (request):
    curso = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'curso': curso})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/crear_curso.html', {'form': form})

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form})


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, 'cursos/eliminar_curso.html', {'curso': curso})

# registro de docentes
def listar_docentes (request):
    docente = Docente.objects.all()
    return render(request, 'docentes/listar_docentes.html', {'docente': docente})

def crear_Docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_docentes')
    else:
        form = DocenteForm()
    return render(request, 'docentes/crear_docente.html', {'form': form})


def editar_Docente(request, id):
    docente = get_object_or_404(Docente, id=id)
    if request.method == 'POST':
        form = DocenteForm(request.POST, request.FILES, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('listar_docentes')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'docentes/editar_docente.html', {'form': form})

def eliminar_Docente(request, id):
    docente = get_object_or_404(Docente, id=id)
    if request.method == 'POST':
        docente.delete()
        return redirect('listar_docentes')
    return render(request, 'docentes/eliminar_docente.html', {'docente': docente})

# registro de estudiantes
def listar_estudiantes (request):
    estudiante = Estudiante.objects.all()
    return render(request, 'estudiantes/listar_estudiantes.html', {'estudiante': estudiante})

def crear_Estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/crear_estudiante.html', {'form': form})

def editar_Estudiante(request, id): 
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes/editar_estudiante.html', {'form': form})

def eliminar_Estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listar_estudiantes')
    return render(request, 'estudiantes/eliminar_estudiante.html', {'estudiante': estudiante})

# registro de inscripciones
def listar_inscripciones (request):
    inscripcion = Inscripcion.objects.all()
    return render(request, 'inscripciones/listar_inscripciones.html', {'inscripcion': inscripcion})

def crear_Inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'inscripciones/crear_inscripcion.html', {'form': form})

def editar_Inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, request.FILES, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'inscripciones/editar_inscripcion.html', {'form': form})

def eliminar_Inscripcion(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('listar_inscripciones')
    return render(request, 'inscripciones/eliminar_inscripcion.html', {'inscripcion': inscripcion})
