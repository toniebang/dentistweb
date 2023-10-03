from django.contrib import admin
from .models import Post, Doctores, Mensaje, Cita, Categoria, Comentario

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
    list_display = ('name', 'address', 'schedule', 'phone_number')
    schedule = 'date'
    
    
    
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'publish_date', 'post', 'status')
    
admin.site.register(Comentario, ComentariosAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)
admin.site.register(Doctores, DoctoresAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Cita, ApointmentAdmin)
