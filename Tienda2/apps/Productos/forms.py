from django import forms
from apps.Productos.models import Producto

class ProductoForm(forms.ModelForm):
	
	class Meta:
		
		model = Producto
		
		fields = [

			'nomProducto',
			'descripcion',
			'costo',
			'disponibilidad',
			'categoria',

		]

		labels = {


			'nomProducto' : 'Nombre del producto',
			'descripcion' :'descripcion del producto',
			'costo' : 'Costo',
			'disponibilidad' : 'Disponibilidad',
			'categoria' : 'Categoria',
		}

		widgets = {

			'nomProducto':forms.TextInput(attrs={'class' : 'form-control'}),
			'descripcion':forms.TextInput(attrs={'class' : 'form-control'}),
			'costo':forms.TextInput(attrs={'class' : 'form-control'}),
			'disponibilidad':forms.TextInput(attrs={'class' : 'form-control'}),
			'categoria':forms.TextInput(attrs={'class' : 'form-control'}),
		

		}
