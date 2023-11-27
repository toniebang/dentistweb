from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contact, name='contact'),
    path('acerca', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('articulo/<int:id>/', views.blog_details, name='blog_details'),
    path('precios', views.pricing, name='pricing'),
    path('servicios', views.service, name='service'),
    path('contact_sent', views.sent, name='sent' ),
    path('contenido_educativo', views.contenido_educativo, name='contenido-educativo'),
    path('curso/<str:titulo>/', views.curso, name='curso' ),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/<uidb64>/<token>/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)