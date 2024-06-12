from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('formulario/', views.formulario, name='formulario'),
    path('contacto/', views.contacto, name='contacto'),
    path('ejemplo/', views.ejemplo, name='ejemplo') 
]

