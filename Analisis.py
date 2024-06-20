import os
from dotenv import load_dotenv
import openai
load_dotenv()

api = os.getenv("API_KEY")



def conversacionResumen(message):
    prompt = "Hola. Eres un doctor oncólogo especializado en cáncer de pulmón. Estás en una consulta médica con un paciente y debes revisar y analizar detenidamente su historia clínica la cual te entrego en forma de lista de diccionarios, donde el ultimo diccionario es mi paciente, así como los datos médicos proporcionados. Tu tarea es elaborar un veredicto de como se encuentra su enfermedad en su estado actual teniendo en cuenta su historia clinica ademas de desarrollar un informe detallado que destaque los puntos más importantes y relevantes de esta información, incluyendo el análisis de datos cuantitativos sobre el tumor, como tamaño, ubicación y características específicas. Asegúrate de considerar todos los aspectos clínicos para ofrecer un resumen preciso para un diagnóstico preciso y recomendaciones adecuadas para el tratamiento."
    lt_mensajes = [
        {"role": "system", "content": prompt},
    ]
    return requestMessage(message, lt_mensajes)

def requestMessage(message,lt_mensajes):
    lt_mensajes.append({"role": "user", "content": message})
    completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= lt_mensajes
    )
    respuesta = completion.choices[0].message.content
    lt_mensajes.append({"role": "assistant", "content": respuesta})
    return respuesta


