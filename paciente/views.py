from django.shortcuts import render
from .serializer import PacienteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .logic.logicPaciente import createPaciente, getPacientes, getPacienteByDocuemnt, deletePacienteByDocument, updatePacienteByDocument

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        try: 
            paciente = createPaciente(request.data)
            serializer = PacienteSerializer(paciente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def pacientesList(request):
    if request.method == 'GET':
        pacientes = getPacientes()
        serializer = PacienteSerializer(pacientes, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def pacienteByDocument(request, document):
    if request.method == 'GET':
        try:
            paciente = getPacienteByDocuemnt(document)
            serializer = PacienteSerializer(paciente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def deletePaciente(request, document):
    if request.method == 'DELETE':
        try:
            deletePacienteByDocument(document)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def updatePaciente(request, document):
    if request.method == 'PUT':
        try:
            updatePacienteByDocument(document, request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
#Additional Functions
"""def validateData(data):
    document = data.get('document', None)
    age = data.get('age', None)
    message = ''
    valid = True
    
    if document:
        client = getPacienteByDocuemnt(document)
        if client is not None:
            message += "The client with the provided document number already exists in the system. "
            valid = False

    if age < 18:
            message += "The client must be of legal age to register in the system. "
            valid = False

    if document:
        if len(document) != 10:
            message += "The document number (cedula) must have 10 digits."
            valid = False

    return valid, message if message else None"""