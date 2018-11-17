from django.contrib import admin

from apps.Productos.models import Producto, Categoria

admin.site.register(Producto)
admin.site.register(Categoria)