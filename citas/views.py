from django.views.decorators.csrf import csrf_exempt
import json
from Analisis import conversacionResumen
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from paciente.models import Paciente
from .logic.logicCita import *


@api_view(["GET"])
def citaList(request):
    citas = getCitas()
    citasList = [{"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData} for cita in citas]
    return Response(citasList, status=status.HTTP_200_OK)

@api_view(["GET"])
def citaDetail(request, pk):
    cita = getCitaByID(pk)
    cita_data = {"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData}
    return Response(cita_data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def citaCreate(request):
    try:
        data = json.loads(request.body)
        cita = createCita(data)
        return Response({"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData}, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["PUT"])
def citaUpdate(request, pk):
    try:
        data = json.loads(request.body)
        cita = updateCita(pk, data)
        return Response({"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData}, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["DELETE"])
def citaDelete(request, pk):
    try:
        deleteCita(pk)
        return Response({"status": "deleted"}, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def citasByPacienteDocumento(request, documento):
    try:
        citas, paciente = getCitasByPacienteDocumento(documento)
        citasList = [{"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData} for cita in citas]
        citasList.append(paciente)
        return Response(citasList, status=status.HTTP_200_OK)
    except Paciente.DoesNotExist:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def obtenerResumen(request, documento):
    try:
        citas, paciente = getCitasByPacienteDocumento(documento)
        citasList = [{"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData} for cita in citas]
        citasList.append(paciente)
        respuesta = conversacionResumen(str(citasList))
        return Response({"mensaje":respuesta},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
