from django.shortcuts import render

# Create your views here.
#vista de la pagina principal
def index(request):
    #render toma el request y el archivo HTML que queremos mostrar
    return render(request, 'home/index.html')

#vista de la pagina de contacto 
def contacto(request):
    return render(request, 'home/contacto.html')