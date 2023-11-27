from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria')
    date_hierarchy = 'fecha_publicacion'


class DoctoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especialidad')
    search_fields = ('id', 'nombre', 'especialidad')

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name')


class ApointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'schedule', 'phone_number', 'leido')
    schedule = 'date'
    
    
    
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'publish_date', 'post', 'status')
    

class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'precio', 'tutor', 'fecha_publicacion')

class CategoriaCursoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class PrecioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'unidad')

class CorreosAdmin(admin.ModelAdmin):
    list_display = ('correos',)

admin.site.register(Comentario, ComentariosAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)
admin.site.register(Doctores, DoctoresAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Cita, ApointmentAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(CategoriaCurso, CategoriaCursoAdmin)
admin.site.register(Precio, PrecioAdmin)
admin.site.register(Correo, CorreosAdmin)
