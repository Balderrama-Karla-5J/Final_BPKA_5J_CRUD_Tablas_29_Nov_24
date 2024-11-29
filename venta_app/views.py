from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.
def inicio_vistaVentas(request):
    lasVentas=Ventas.objects.all()
    return render(request,"gestionarVentas.html", {"misVentas":lasVentas})

def registrarVentas(request):
    id_venta=request.POST["id_venta"]
    id_libro=request.POST["numid_libro"]
    fecha=request.POST["datefecha"]
    cantidad=request.POST["numcantidad"]
    precio=request.POST["numprecio"]
    id_cliente=request.POST["id_cliente"]
    id_empleado=request.POST["id_empleado"]
    
    guardarVentas=Ventas.objects.create(
        id_venta=id_venta,id_libro=id_libro,fecha=fecha,cantidad=cantidad,precio=precio,
        id_cliente=id_cliente,id_empleado=id_empleado
    ) #GUARDA EL REGISTRO
    
    return redirect("ventas")

def seleccionarVentas(request,id_venta):
    ventas=Ventas.objects.get(id_venta=id_venta)
    fecha_venta = ventas.fecha.strftime('%Y-%m-%d')
    return render(request, "editarVentas.html",{"misVentas":ventas, "misVentas":ventas,"fecha_venta":fecha_venta})

def editarVentas(request):
    id_venta=request.POST["id_venta"]
    id_libro=request.POST["numid_libro"]
    fecha=request.POST["datefecha"]
    cantidad=request.POST["numcantidad"]
    precio=request.POST["numprecio"]
    id_cliente=request.POST["id_cliente"]
    id_empleado=request.POST["id_empleado"]
    
    ventas=Ventas.objects.get(id_venta=id_venta)
    ventas.id_venta=id_venta
    ventas.id_libro=id_libro
    ventas.fecha=fecha
    ventas.cantidad=cantidad
    ventas.precio=precio
    ventas.id_cliente=id_cliente
    ventas.id_empleado=id_empleado
    ventas.save() #guarda registro actualizado
    return redirect("ventas")

def borrarVentas(request,id_venta):
    ventas=Ventas.objects.get(id_venta=id_venta)
    ventas.delete() # borra el registro
    return redirect("ventas")