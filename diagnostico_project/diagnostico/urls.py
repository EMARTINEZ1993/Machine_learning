from django.urls import path, include
from . import views

urlpatterns = [


    path('diagnostico/', views.diagnostico, name='diagnostico'),

]
