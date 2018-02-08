from django.shortcuts import render
from encuesta.models import Pregunta

# Create your views here.
def lista_preguntas(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'encuesta/lista_preguntas.html', {'preguntas':preguntas})