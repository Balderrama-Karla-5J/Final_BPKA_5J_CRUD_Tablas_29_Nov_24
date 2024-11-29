from django.urls import path
from empleado_app import views

urlpatterns = [
   path("empleados", views.inicio_vistaEmpleados, name= "empleados" ),
   path("registrarEmpleados/",views.registrarEmpleados,name="registrarEmpleados"),
      path("seleccionarEmpleados/<id_empleado>",views.seleccionarEmpleados,name="seleccionarEmpleados"),
   path("editarEmpleados/",views.editarEmpleados,name="editarEmpleados"),
   path("borrarEmpleados/<id_empleado>",views.borrarEmpleados,name="borrarEmpleados"),
   ]