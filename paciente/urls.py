from django.urls import path
from .views import create, getPacientes, getPacienteByDocuemnt, updatePaciente, deletePaciente

urlpatterns = [
    path('pacientes/', getPacientes),
    path('pacientes/createPacientes/', create),  
    path('pacientes/<int:document>/', getPacienteByDocuemnt),  
    path('pacientes/deleteClient/<int:document>/', deletePaciente),  
    path('pacientes/updateClient/<int:document>/', updatePaciente), 
]