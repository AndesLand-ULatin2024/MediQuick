from ..models import Paciente

def createPaciente(data):
    try:
        return Paciente.objects.create(data)
    except: 
        raise Exception({'error':'Error al crear Paciente'},404)

def getPacientes():
    return Paciente.objects.all().order_by('name')

def getPacienteByDocuemnt(docuemnt):
    try:
        return Paciente.objects.get(docuemnt=docuemnt)
    except:
        raise Exception({'error':'Hubo un error, el Paciente no existe'},404)

def deletePacienteByDocument(document):
    try:
        Paciente.objects.get(document=document).delete()
    except:
        raise Exception({'error':'No fue posible borrar el Paciente'},404)

def updatePacienteByDocument(data):
    try:
        paciente = Paciente.objects.get(data['document'])
        setattr(paciente, data)
        paciente.save()
        return paciente
    except:
        raise Exception({'error':'No fue posible actualizar el Paciente'},404)