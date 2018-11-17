from django.urls import path
from apps.Productos.views import index, invproductos, invcategorias, viewProductos, viewCategorias, nuevoRegistro, editarRegistro,eliminarRegistro
app_name = 'Productos'
urlpatterns = [
  	path('', index),
    path('index', index),
    path('invproductos', viewProductos.as_view(), name="listaProductos"),
    path('invcategorias', viewCategorias.as_view()),
    path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
    path('editarRegistro/<id>', editarRegistro, name="editarRegistro"),
    path('elminarRegistro/<id>', eliminarRegistro, name="eliminarRegistro"),
]