from django.shortcuts import render, redirect
from .models import Sucursal

# Create your views here.
def inicio_vistaSucursal(request):
    losSuc=Sucursal.objects.all()
    return render(request,"gestionarSucursal.html", {"misSucursal":losSuc})

def registrarSucursal(request):
    id_sucursal=request.POST["id_sucursal"]
    txtdireccion=request.POST["txtdireccion"]
    numtelefono=request.POST["numtelefono"]
    txtcorreo=request.POST["txtcorreo"]
    numstock=request.POST["numstock"]
    numempleados=request.POST["numempleados"]
    txthorario=request.POST["txthorario"]
    
    guardarSucursal=Sucursal.objects.create(
        id_sucursal=id_sucursal,txtdireccion=txtdireccion,numtelefono=numtelefono,txtcorreo=txtcorreo,numstock=numstock,
        numempleados=numempleados,txthorario=txthorario
    ) #GUARDA EL REGISTRO
    
    return redirect("sucursales")

def seleccionarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarSucursal.html",{"misSucursal":sucursal})

def editarSucursal(request):
    id_sucursal=request.POST["id_sucursal"]
    txtdireccion=request.POST["txtdireccion"]
    numtelefono=request.POST["numtelefono"]
    txtcorreo=request.POST["txtcorreo"]
    numstock=request.POST["numstock"]
    numempleados=request.POST["numempleados"]
    txthorario=request.POST["txthorario"]
    
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.id_sucursal=id_sucursal
    sucursal.txtdireccion=txtdireccion
    sucursal.numtelefono=numtelefono
    sucursal.txtcorreo=txtcorreo
    sucursal.numstock=numstock
    sucursal.numempleados=numempleados
    txthorario=request.POST["txthorario"]
    sucursal.txthorario=txthorario
    sucursal.save() #guarda registro actualizado
    return redirect("sucursales")

def borrarSucursal(request,id_sucursal):
    sucursales=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursales.delete() # borra el registro
    return redirect("sucursales")