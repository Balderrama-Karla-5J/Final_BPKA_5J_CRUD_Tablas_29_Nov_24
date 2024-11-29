from django.shortcuts import render, redirect
from .models import Clientes

# Create your views here.
def inicio_vistaClientes(request):
    losClientes=Clientes.objects.all()
    return render(request,"gestionarClientes.html", {"misClientes":losClientes})

def registrarClientes(request):
    id_cliente=request.POST["numidcliente"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefoto"]
    correo=request.POST["txtcorreo"]
    edad=request.POST["numedad"]
    sexo=request.POST["txtsexo"]
    
    guardarClientes=Clientes.objects.create(
        id_cliente=id_cliente,nombre=nombre,direccion=direccion,telefono=telefono,correo=correo,
        edad=edad,sexo=sexo
    ) #GUARDA EL REGISTRO
    
    return redirect("clientes")

def seleccionarClientes(request,id_cliente):
    clientes=Clientes.objects.get(id_cliente=id_cliente)
    return render(request, "editarClientes.html",{"misClientes":clientes})

def editarClientes(request):
    id_cliente=request.POST["numidcliente"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefoto"]
    correo=request.POST["txtcorreo"]
    edad=request.POST["numedad"]
    sexo=request.POST["txtsexo"]
    
    clientes=Clientes.objects.get(id_cliente=id_cliente)
    clientes.nombre=nombre
    clientes.direccion=direccion
    clientes.telefono=telefono
    clientes.correo=correo
    clientes.edad=edad
    clientes.sexo=sexo
    clientes.save() #guarda registro actualizado
    return redirect("clientes")

def borrarClientes(request,id_cliente):
    clientes=Clientes.objects.get(id_cliente=id_cliente)
    clientes.delete() # borra el registro
    return redirect("clientes") 