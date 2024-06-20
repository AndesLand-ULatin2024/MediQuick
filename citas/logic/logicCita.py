from django.http import HttpResponseBadRequest
from citas.models import Citas
from paciente.models import Paciente
from paciente.serializer import PacienteSerializer

def getCitas():
    return Citas.objects.all().order_by("date")

def getCitaByID(citaID):
    try:
        return Citas.objects.get(id=citaID)
    except:
        raise Exception({"error": "Cita no encontrada"}, 404)
    

def createCita(data):
    try:
        paciente = Paciente.objects.get(document=data['paciente'])
        data['paciente'] = paciente
        cita = Citas.objects.create(**data)
        return cita
    except:
        raise Exception({"error": "Error al crear cita"}, 404)

def updateCita(citaID, data):
    try:
        cita = Citas.objects.get(id=citaID)
        paciente = Paciente.objects.get(document=data['paciente'])
        data['paciente'] = paciente
        for key, value in data.items():
            setattr(cita, key, value)
        cita.save()
        return cita
    except:
        raise Exception({"error": "Error al actualizar cita"}, 404)

def deleteCita(citaID):
    try:
        cita = Citas.objects.get(id=citaID)
        cita.delete()
    except:
        raise Exception({"error": "Error al eliminar cita"}, 404)
    
def getCitasByPacienteDocumento(document):
    paciente = Paciente.objects.get(document=document)
    serializer = PacienteSerializer(paciente)
    return Citas.objects.filter(paciente=paciente), serializer.data

