from django.http import HttpResponse

def vista_uno(request):
    return HttpResponse("Hola desde la Vista 1 de App A")

def vista_dos(request):
    return HttpResponse("Hola desde la Vista 2 de App A")