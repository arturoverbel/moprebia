from django.http import HttpResponse


def index(request):
    return HttpResponse("Servicio recibe 2 parametros")

def getData(request, frecuencia, porcentaje):

    return HttpResponse("Se recibe frecu " + frecuencia + " y " + porcentaje)