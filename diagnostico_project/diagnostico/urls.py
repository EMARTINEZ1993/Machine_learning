from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
     path('historial/', views.lista_diagnosticos, name='lista_diagnosticos'),
]
