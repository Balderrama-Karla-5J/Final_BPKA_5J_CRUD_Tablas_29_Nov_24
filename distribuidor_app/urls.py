from django.urls import path
from distribuidor_app import views

urlpatterns = [
path("distribuidores", views.inicio_vistaDistribuidor, name= "distribuidores" ),
path("registrarDistribuidor/",views.registrarDistribuidor,name="registrarDistribuidor"),
    path("seleccionarDistribuidor/<id_distribuidor>",views.seleccionarDistribuidor,name="seleccionarDistribuidor"),
path("editarDistribuidor/",views.editarDistribuidor,name="editarDistribuidor"),
path("borrarDistribuidor/<id_distribuidor>",views.borrarDistribuidor,name="borrarDistribuidor"),
]