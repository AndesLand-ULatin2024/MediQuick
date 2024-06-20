from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from Analisis import conversacionResumen

from paciente.models import Paciente
from .logic.logicCita import *


@require_http_methods(["GET"])
def citaList(request):
    citas = getCitas()
    citasList = [{"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData} for cita in citas]
    return JsonResponse(citasList, safe=False)

@require_http_methods(["GET"])
def citaDetail(request, pk):
    cita = getCitaByID(pk)
    cita_data = {"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData}
    return JsonResponse(cita_data)

@csrf_exempt
@require_http_methods(["POST"])
def citaCreate(request):
    try:
        data = json.loads(request.body)
        cita = createCita(data)
        return JsonResponse({"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData})
    except Exception as e:
        return HttpResponseBadRequest(str(e))

@csrf_exempt
@require_http_methods(["PUT"])
def citaUpdate(request, pk):
    try:
        data = json.loads(request.body)
        cita = updateCita(pk, data)
        return JsonResponse({"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData})
    except Exception as e:
        return HttpResponseBadRequest(str(e))

@csrf_exempt
@require_http_methods(["DELETE"])
def citaDelete(request, pk):
    try:
        deleteCita(pk)
        return JsonResponse({"status": "deleted"})
    except Exception as e:
        return HttpResponseBadRequest(str(e))

@require_http_methods(["GET"])
def citasByPacienteDocumento(request, documento):
    try:
        citas, paciente = getCitasByPacienteDocumento(documento)
        citasList = [{"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData} for cita in citas]
        citasList.append(paciente)
        return JsonResponse(citasList, safe=False)
    except Paciente.DoesNotExist:
        return HttpResponseNotFound()

@require_http_methods(["GET"])
def obtenerResumen(request, documento):
    try:
        citas, paciente = getCitasByPacienteDocumento(documento)
        citasList = [{"id": cita.id, "date": cita.date, "reason": cita.reason, "treatment": cita.treatment, "examsData": cita.examsData} for cita in citas]
        citasList.append(paciente)
        respuesta = conversacionResumen(str(citasList))
        return JsonResponse({"mensaje":respuesta})
    except Exception as e:
        return HttpResponseBadRequest(str(e))
