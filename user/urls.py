from django.urls import path
from . import views


urlpatterns = [
    path('', views.perfil, name='perfil'),
    path('crear-usuario', views.crear_usuario, name='crear_usuario'),
  
]