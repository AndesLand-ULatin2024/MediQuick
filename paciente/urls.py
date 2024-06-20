from django.urls import path
from .views import create, pacientesList, pacienteByDocument, updatePaciente, deletePaciente

urlpatterns = [
    path('pacientes/', pacientesList),
    path('pacientes/createPacientes/', create),  
    path('pacientes/<int:document>/', pacienteByDocument),  
    path('pacientes/deletePaciente/<int:document>/', deletePaciente),  
    path('pacientes/updatePaciente/<int:document>/', updatePaciente), 
]