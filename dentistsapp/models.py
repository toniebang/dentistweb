from django.db import models
from ckeditor.fields import RichTextField

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
    schedule = models.CharField('Date', max_length=40, blank=True, null=True)
    
    
   

    def __str__(self) -> str:
      return 'Appointment on :' + str(self.schedule) 

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    name = models.CharField(max_length=40)
    email = models.EmailField()
    content = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
      return f'Comentario de {self.name}'
