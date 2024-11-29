from django.shortcuts import render, redirect
from .models import Distribuidor

# Create your views here.
def inicio_vistaDistribuidor(request):
    losDistribuidor=Distribuidor.objects.all()
    return render(request,"gestionarDistribuidor.html", {"misDistribuidor":losDistribuidor})

def registrarDistribuidor(request):
    id_distribuidor=request.POST["id_distribuidor"]
    costo=request.POST["numcosto"]
    numentregas=request.POST["numentregas"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    nombre=request.POST["txtnombre"]
    ciudad=request.POST["txtciudad"]
    
    guardarDistribuidor=Distribuidor.objects.create(
        id_distribuidor=id_distribuidor,costo=costo,numentregas=numentregas,telefono=telefono,correo=correo,
        nombre=nombre,ciudad=ciudad
    ) #GUARDA EL REGISTRO
    
    return redirect("distribuidores")

def seleccionarDistribuidor(request,id_distribuidor):
    distribuidores=Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    return render(request, "editarDistribuidor.html",{"misDistribuidor":distribuidores})

def editarDistribuidor(request):
    id_distribuidor=request.POST["id_distribuidor"] #Verificar
    costo=request.POST["numcosto"]
    numentregas=request.POST["numentregas"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    nombre=request.POST["txtnombre"]
    ciudad=request.POST["txtciudad"]
    
    distribuidor=Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    distribuidor.costo=costo
    distribuidor.numentregas=numentregas
    distribuidor.telefono=telefono
    distribuidor.correo=correo
    distribuidor.nombre=nombre
    distribuidor.ciudad=ciudad
    distribuidor.save() #guarda registro actualizado
    return redirect("distribuidores")

def borrarDistribuidor(request,id_distribuidor):
    distribuidor=Distribuidor.objects.get(id_distribuidor=id_distribuidor)
    distribuidor.delete() # borra el registro
    return redirect("distribuidores")