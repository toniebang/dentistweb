from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog_details/<int:id>/', views.blog_details, name='blog_details'),
    path('pricing', views.pricing, name='pricing'),
    path('service', views.service, name='service'),
    path('contact_sent', views.sent, name='sent' ),
    path('tienda', views.tienda, name='tienda' ),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)