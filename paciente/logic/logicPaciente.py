from ..models import Paciente

def getPacientes():
    return Paciente.objects.all().order_by('name')

def createPaciente(data):
    try:
        return Paciente.objects.create(data)
    except: 
        raise Exception({'error':'Error al crear Paciente'})