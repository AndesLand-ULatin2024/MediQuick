from ..models import Paciente

def createPaciente(data):
    try:
        return Paciente.objects.create(**data)
    except: 
        raise Exception({'error':'Error al crear Paciente'},404)

def getPacientes():
    return Paciente.objects.all().order_by('name')

def getPacienteByDocuemnt(document):
    try:
        return Paciente.objects.get(document=document)
    except:
        raise Exception({'error':'Hubo un error, el Paciente no existe'},404)

def deletePacienteByDocument(document):
    try:
        Paciente.objects.get(document=document).delete()
    except:
        raise Exception({'error':'No fue posible borrar el Paciente'},404)

def updatePacienteByDocument(document, data):
    try:
        paciente = Paciente.objects.get(document=document)
        for key, value in data.items():
            setattr(paciente, key, value)
        paciente.save()
        return paciente
    except:
        raise Exception({'error':'No fue posible actualizar el Paciente'},404)