from collections.abc import Iterable
from django.db import models
from django_resized import ResizedImageField
from PIL import Image
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Post(models.Model):
    id = models.AutoField('id',primary_key=True)
    previa = models.CharField('Previa de Post', max_length=200)
    imagen = models.ImageField('Portada')
    titulo = models.CharField('Titulo de post', max_length=250) 
    contenido = RichTextField('Contenido', max_length=7000)
    fecha_publicacion = models.DateField('Fecha de Publicacion',  auto_now_add=True)
    
    
    # foreignkeys
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    

class Doctores(models.Model):
    id = models.AutoField('id Doctor', primary_key=True)
    foto = models.ImageField(upload_to='doctores')
    nombre = models.CharField('Nombre', max_length=50)
    especialidad = models.CharField('Especialidad', max_length=50)

    def __str__(self):
        return 'Dr ' + self.nombre
    

class Mensaje(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField('Contenido de Mensaje')
    date = models.DateField('Fecha', auto_now_add=True)

    def __str__(self) -> str:
        return 'Mensaje de: ' + self.name + ' el dia ' + str(self.date)
    
  

class Cita(models.Model):
    topics=[
        ('Asunto', 'Asunto (Click para seleccionar)'),
        ('No especificado', 'No especificado'),
        ('Dolor de cabeza', 'Dolor de cabeza'),
        ('Dolor de vientre', 'Dolor de vientre'),
        ('fiebre', 'fiebre'),
        ('otro', 'otro')
    ]
 
    name = models.CharField(max_length=40)
    asunto = models.CharField('Asunto', max_length=45, blank=True, null=True, choices=topics, default='Asunto')
    phone_number = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    email = email = models.EmailField()
    message = models.TextField('Mensaje')
    schedule = models.CharField('Fecha', max_length=40, blank=True, null=True)
    leido = models.BooleanField('Leido', default=False)

    
    
   

    def __str__(self) -> str:
      return 'Appointment on :' + str(self.schedule) 

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    # name = models.CharField(max_length=100)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    content = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
      return f'Comentario de {self.name}'



# ========== CURSOS ==================

class CategoriaCurso(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
      return self.nombre

class Curso(models.Model):
    titulo = models.CharField(max_length=255, blank=False, null=False)
    imagen = ResizedImageField('Imagen', size=[1140, 1521], upload_to='cursos')
    categoria = models.ForeignKey(CategoriaCurso, on_delete=models.CASCADE, related_name='categoriacurso')
    descuentos = models.BooleanField('Curso Disponible', default=True)
    precio = models.FloatField('Precio')
    fecha_publicacion = models.DateField(auto_now_add=True)
    acerca =  RichTextField('Contenido', max_length=15000)
    duracion = models.CharField('Duracion de Curso', max_length=255)
    tutor = models.CharField('Profesor', max_length=200)
    enlace = models.CharField('Enlace de pago', max_length=1000, default='N/A')
    lecciones = RichTextField('Lecciones', max_length=15000, default='N/A')
    publico = RichTextField('Público objetivo', max_length=15000, default='N/A')

    def __str__(self) -> str:
      return self.titulo
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
        
    #     if self.imagen:
    #         output_size = (1140, 1521)
    #         image = Image.open(self.imagen.path)
    #         image.thumbnail(output_size)
    #         image.save(self.imagen.path)


class Precio(models.Model):
    nombre = models.CharField('Nombre del servicio',max_length=200)
    unidad = models.CharField('Unidad', max_length=200)
    precio = models.IntegerField('Precio')
    
    def __str__(self) -> str:
      return self.nombre


class Correo(models.Model):
    correos = models.EmailField('Correos')

    def __str__(self) -> str:
      return self.correos