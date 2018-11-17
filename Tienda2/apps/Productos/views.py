from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from apps.Productos.models import Producto, Categoria
from apps.Productos.forms import ProductoForm
# Create your views here.
def index(request):
	return HttpResponse("Esta es la respuesta");


def invproductos(request):
	contexto = {
		'Productos':Producto.objects.all()
	} 
	return render(request, 'tablas/productos.html', contexto)

def invcategorias(request):
	contexto = {
		'Productos':Categoria.objects.all()
	} 
	return render(request, 'tablas/categorias.html', contexto)


# Formulario
def nuevoRegistro(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect ('Productos:listaProductos')
	else:
		form = ProductoForm()
	return render(request, 'tablas/productoForm.html', {'form':form});

def editarRegistro(request, id):
	producto = Producto.objects.get(id=id)
	if request.method == 'GET':
		form = ProductoForm(instance = producto)
	else:
		form = ProductoForm(request.POST, instance = producto)
		if form.is_valid():
			form.save()
		return redirect ('Productos:listaProductos')
	return render(request, 'tablas/productoForm.html', {'form':form})

def eliminarRegistro(request, id):
	producto = Producto.objects.get(id=id).delete()
	return redirect('Productos:listaProductos')

#Formulario

class viewProductos(ListView):
	model= Producto
	queryset = Producto.objects.filter(categoria_id='1')
	template_name = 'tablas/productos.html'

class viewCategorias(ListView):
	model= Categoria
	# queryset = Cliente.objects.filter(nombre='roberto') esta linea solo muestra los robertos
	template_name = 'tablas/categorias.html'
