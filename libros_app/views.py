from django.shortcuts import render, redirect
from .models import Libros

# Create your views here.
def inicio_vistaLibros(request):
    losLibros=Libros.objects.all()
    return render(request,"gestionarLibros.html", {"misLibros":losLibros})

def registrarLibros(request):
    id_libro=request.POST["numid_libro"]
    titulo=request.POST["txttitulo"]
    autor=request.POST["txtautor"]
    ilustrador=request.POST["txtilustrador"]
    año=request.POST["dateaño"]
    precio=request.POST["numprecio"]
    stock=request.POST["numstock"]
    
    guardarLibros=Libros.objects.create(
        id_libro=id_libro,titulo=titulo,autor=autor,ilustrador=ilustrador,año=año,
        precio=precio,stock=stock
    ) #GUARDA EL REGISTRO
    
    return redirect("libros")

def seleccionarLibros(request,id_libro):
    libros=Libros.objects.get(id_libro=id_libro)
    fecha_libro = libros.año.strftime('%Y-%m-%d')
    return render(request, "editarLibros.html",{"misLibros":libros, "misLibros":libros,"fecha_libro":fecha_libro})

def editarLibros(request):
    id_libro=request.POST["numid_libro"]
    titulo=request.POST["txttitulo"]
    autor=request.POST["txtautor"]
    ilustrador=request.POST["txtilustrador"]
    año=request.POST["dateaño"]
    precio=request.POST["numprecio"]
    stock=request.POST["numstock"]
    
    libros=Libros.objects.get(id_libro=id_libro)
    libros.titulo=titulo
    libros.autor=autor
    libros.ilustrador=ilustrador
    libros.año=año
    libros.precio=precio
    libros.stock=stock
    libros.save() #guarda registro actualizado
    return redirect("libros")

def borrarLibros(request,id_libro):
    libros=Libros.objects.get(id_libro=id_libro)
    libros.delete() # borra el registro
    return redirect("libros")