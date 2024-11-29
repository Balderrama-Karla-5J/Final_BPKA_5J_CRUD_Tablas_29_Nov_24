from django.shortcuts import render, redirect
from .models import Empleados

# Create your views here.
def inicio_vistaEmpleados(request):
    losEmpleados=Empleados.objects.all()
    return render(request,"gestionarEmpleados.html", {"misEmpleados":losEmpleados})

def registrarEmpleados(request):
    id_empleado=request.POST["numid_empleado"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefoto"]
    salario=request.POST["numsalario"]
    edad=request.POST["numedad"]
    sexo=request.POST["txtsexo"]
    
    guardarEmpleados=Empleados.objects.create(
        id_empleado=id_empleado,nombre=nombre,direccion=direccion,telefono=telefono,salario=salario,
        edad=edad,sexo=sexo
    ) #GUARDA EL REGISTRO
    
    return redirect("empleados")

def seleccionarEmpleados(request,id_empleado):
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleados.html",{"misEmpleados":empleados})

def editarEmpleados(request):
    id_empleado=request.POST["numid_empleado"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefoto"]
    salario=request.POST["numsalario"]
    edad=request.POST["numedad"]
    sexo=request.POST["txtsexo"]
    
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    empleados.nombre=nombre
    empleados.direccion=direccion
    empleados.telefono=telefono
    empleados.salario=salario
    empleados.edad=edad
    empleados.sexo=sexo
    empleados.save() #guarda registro actualizado
    return redirect("empleados")

def borrarEmpleados(request,id_empleado):
    empleados=Empleados.objects.get(id_empleado=id_empleado)
    empleados.delete() # borra el registro
    return redirect("empleados") 