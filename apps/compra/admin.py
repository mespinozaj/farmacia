from django.contrib import admin
from . models import *
# Register your models here.


class DetalleCompraInLine(admin.TabularInline):
	
	model = DetalleCompra
	extra = 1

	fields = [

		'comprobantecompra',
		'producto', 
		'numeroloteproducto',
		'cantidad',
		'fechavencimiento',
		'ubicacion',
		'preciocompra', 
		'precioventa',
		'subtotal'
	]

	readonly_fields = ['subtotal']
	#campo de solo lectura

	autocomplete_fields = ['producto']
	#autocompletar 

class ComprobanteCompraAdmin(admin.ModelAdmin):

	inlines = [DetalleCompraInLine]
	readonly_fields = ['total']
	
	list_display = ['proveedor', 'fecha']
	list_per_page = 15
	ordering = ['-fecha']
	autocomplete_fields = ['proveedor']
	#autocompletar




admin.site.register(ComprobanteCompra, ComprobanteCompraAdmin)