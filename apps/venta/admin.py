from django.contrib import admin
from .models import *
# Register your models here.


class DetalleVentaInLine(admin.TabularInline):
	
	model = DetalleVenta
	extra = 1

	fields = [

		'comprobanteventa',
		'producto',
		'numerolote', 
		'cantidad',
		'subtotal',

	]

	readonly_fields = ['subtotal']
	#campo de solo lectura

	autocomplete_fields = ['producto']
	#comando para autocompletar


class ComprobanteVentaAdmin(admin.ModelAdmin):

	inlines = [DetalleVentaInLine]
	readonly_fields = ['total']
	#campo de solo lectura

	
	list_display = ['cliente', 'fecha']
	list_per_page = 15
	#listados por pagina
	ordering = ['-fecha']
	#autocomplete_fields = ['cliente']



admin.site.register(ComprobanteVenta, ComprobanteVentaAdmin)	