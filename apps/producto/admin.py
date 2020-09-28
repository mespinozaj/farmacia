from django.contrib import admin
from .models import *

# Register your models here.
class DetalleProductoInLine(admin.TabularInline):
	
	model = DetalleProducto
	extra = 1

	fields = [

		'producto',
		'numeroloteproducto', 
		'cantidad',
		'preciocompra',
		'precioventa',
		'fechavencimiento',
		'fechacompra',
		'ubicacion',
	]

	readonly_fields = ['producto', 
						'numeroloteproducto', 
						'cantidad',
						'preciocompra',
						'precioventa',
						'fechavencimiento',
						'fechacompra',
						'ubicacion',
						]

	


class ProductoAdmin(admin.ModelAdmin):

	search_fields = ['nombre']
	inlines = [DetalleProductoInLine]
	list_per_page = 15
	autocomplete_fields = ['laboratorio', 'tipopresentacion']
	readonly_fields = ['existencia']
	#autocompletar 

class UbicacionAdmin(admin.ModelAdmin):

	search_fields = ['nombre']
	# inlines = [DetalleProductoInLine]
	list_per_page = 15

class LaboratorioAdmin(admin.ModelAdmin):

	search_fields = ['nombre']
	# inlines = [DetalleProductoInLine]
	list_per_page = 15

class TipoPresentacionAdmin(admin.ModelAdmin):

	search_fields = ['nombre']
	# inlines = [DetalleProductoInLine]
	list_per_page = 15


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(TipoPresentacion, TipoPresentacionAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)

# Register your models here.

