from django.db import models
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado
from apps.producto.models import Producto, DetalleProducto
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.

class ComprobanteVenta(models.Model):
	fecha = models.DateField('Fecha', default=date.today,
		null=False, blank=False)
	cliente = models.ForeignKey(
		Cliente, on_delete=models.CASCADE, null=False, blank=False)
	empleado = models.ForeignKey(
		Empleado, on_delete=models.CASCADE, null=False, blank=False)
	total = models.FloatField(
		'total', null=True, blank=True, default=0.00)


	class Meta():
		db_table = 'comprobanteventa'
		verbose_name = 'Comprobante Venta'
		verbose_name_plural = 'Comprobante de Venta'

class DetalleVenta(models.Model):
	
	comprobanteventa = models.ForeignKey(
		ComprobanteVenta, on_delete=models.CASCADE, 
		null=True, blank=True,
		related_name='Detalle')
	producto = models.ForeignKey(
		Producto, on_delete=models.CASCADE, null=False, blank=False)
	numerolote = models.CharField('Numero de lote', null=False, blank=False, 
		max_length=10)
	cantidad = models.PositiveIntegerField('Cantidad',
		null=False, blank=False)
	subtotal = models.FloatField(
		'subtotal', null=True, blank=True, default=0.00)


	class Meta():
		db_table = 'detalleventa'
		verbose_name = 'Detalle venta'
		verbose_name_plural = 'Detalle de ventas'

	def clean(self):
		mp = DetalleProducto.objects.filter(producto = self.producto).filter(numeroloteproducto = self.numerolote).first()
		
		if mp: 	
			
			pro = Producto.objects.filter(nombre = self.producto.nombre).first()
			print(pro)


			if pro.existencia <= self.cantidad: 	
				
				raise ValidationError('No hay existencias')
				
				()	
			else: 

				if mp.cantidad <= self.cantidad:

					raise ValidationError('No hay la existencia suficiente en este detalle')

				else:

					if mp.fechavencimiento <= date.today():

						raise ValidationError('El producto ya esta vencido')

					else:

						print(pro.existencia)


		else: 
			raise ValidationError('El numero de lote no existe')

		
		
	def save (self, force_insert=False, force_update=False, using=None):

		product = DetalleProducto.objects.filter(producto = self.producto).filter(numeroloteproducto = self.numerolote).first()
		print(product)
		print(product.producto)
		print(product.precioventa)
		self.subtotal = (self.cantidad * product.precioventa)

		rest = Producto.objects.filter(nombre = self.producto).first()
		rest.existencia = (rest.existencia - self.cantidad)
		print(rest.existencia)
		product.cantidad = (product.cantidad - self.cantidad)
		rest.save()
		product.save()
		
		comproventa = ComprobanteVenta.objects.filter(id=self.comprobanteventa.id).first()
		print(comproventa.fecha)
		comproventa.total = (comproventa.total + self.subtotal)
		comproventa.save()
		super(DetalleVenta, self).save(force_insert, force_update, using)








