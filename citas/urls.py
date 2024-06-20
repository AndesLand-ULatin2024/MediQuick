from django.urls import path
from .views import *

urlpatterns = [
    path('citas/', citaList, name='citaList'),
    path('citas/<int:pk>/', citaDetail, name='citaDetail'),
    path('citas/new/', citaCreate, name='citaCreate'),
    path('citas/<int:pk>/edit/', citaUpdate, name='citaUpdate'),
    path('citas/<int:pk>/delete/', citaDelete, name='citaDelete'),
    path('citas/paciente/<int:documento>/', citasByPacienteDocumento, name='citasByPacienteDocumento'),
    path('citas/paciente/<int:documento>/analisis/', obtenerResumen, name='obtenerResumen'),
]