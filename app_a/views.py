from django.shortcuts import render

def home(request):
    contexto = {
        'mensaje': '¡Hola! Logré conectar la aplicación correctamente. Objetivo cumplido.',
        'autor': 'Jose Sepulveda'
    }
    return render(request, 'home.html', contexto)