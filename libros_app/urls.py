from django.urls import path
from libros_app import views

urlpatterns = [
   path("libros", views.inicio_vistaLibros, name= "libros" ),
   path("registrarLibros/",views.registrarLibros,name="registrarLibros"),
      path("seleccionarLibros/<id_libro>",views.seleccionarLibros,name="seleccionarLibros"),
   path("editarLibros/",views.editarLibros,name="editarLibros"),
   path("borrarLibros/<id_libro>",views.borrarLibros,name="borrarLibros"),
   ]