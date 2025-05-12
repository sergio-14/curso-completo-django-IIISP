from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Docente(models.Model):
    TITULO = [
        ('Lic.', 'Licenciatura'),
        ('Ing.', 'Ingeniería'),
        ('Mtra.', 'Maestría'),
        ('Dr.', 'Doctorado'),
       
    ]
    usuario_d = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_d = models.ImageField(upload_to='docente', null=True, blank=True)
    especialidad = models.CharField(max_length=100)
    titulo = models.CharField(max_length=10, choices=TITULO)
    
    def __str__(self):
        return f'{self.titulo} {self.usuario_d.last_name} {self.usuario_d.first_name} '
    
class Estudiante(models.Model):
    usiuario_e = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_e  = models.ImageField(upload_to='estudiantes', null=True, blank=True)
    matricula = models.CharField(max_length=10, null=True, blank=True ,unique=True)
    
    def __str__(self):
        return f"{self.usiuario_e.first_name}  {self.usiuario_e.last_name} "
    
class Curso(models.Model):
    NIVEL_CHOICES = [
        ('Basico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]
    
    titulo = models.CharField(max_length=400, null=True, blank=True)
    imagen_portada = models.ImageField(upload_to='cursos', null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    nivel = models.CharField(max_length=15, choices=NIVEL_CHOICES, null=True, blank=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True, blank=True)
    duracion = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.titulo}"
    
class Inscripcion (models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Finalizado', 'Finalizado'),
        ('Suspendido', 'Suspendido'),
    ]
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, null=True, blank=True)
    precio_total = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.estudiante} - {self.curso} - {self.fecha_inscripcion}"