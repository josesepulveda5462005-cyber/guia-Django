from django.urls import path
from . import views

urlpatterns = [
    path('uno/', views.vista_uno, name='vista_uno'),
    path('dos/', views.vista_dos, name='vista_dos'),
]