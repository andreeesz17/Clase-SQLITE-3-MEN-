from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def hola_mundo(request):
    html = """
    <h1>Hola Bienvenidos<h1>
    <p>
    CAMINO   A   DEVELOPER   PANAS
    </p>
    """
    
    return HttpResponse(html)
    
# Create your views here.
