from django.db import models

# Create your models here.
class TipoPresentacion(models.Model):
	tipopresentacion = models.CharField('Tipo de Presentacion', 
		null=False, blank=False, max_length=20, unique=True)

	def __str__(self):
		return self.tipopresentacion

	class Meta ():
		db_table = 'tipopresentacion'
		verbose_name = 'Tipo Presentacion'
		verbose_name_plural = 'Tipo de Presentacion'


class Ubicacion(models.Model):
	
	estante = models.PositiveIntegerField('Numero de estante', 
		null=False, blank=False, default='')
	fila = models.PositiveIntegerField('Numero de fila',
		null=False, blank=False, default='')

	def __str__(self):
		return "estante %s fila %s "% (self.estante, self.fila)


	class Meta ():
		db_table = 'ubicacion'
		verbose_name = 'Ubicacion'
		verbose_name_plural = 'Ubicaciones'



class Laboratorio(models.Model):
	
	nombre = models.CharField('Nombre del laboratorio', null=False, blank=False,
		max_length=20, unique=True)

	def __str__(self):
		return "%s "% (self.nombre)

	class Meta():
		db_table = 'laboratorio'
		verbose_name = 'Laboratorio'
		verbose_name_plural = 'Laboratorios'


class Producto(models.Model):
	nombre = models.CharField('nombre', null=False, blank=False, 
		max_length=100)
	laboratorio = models.ForeignKey(
		Laboratorio, on_delete=models.CASCADE, null=False, blank=False)
	tipopresentacion = models.ForeignKey(
		TipoPresentacion, on_delete=models.CASCADE, null=False, blank=False)
	existencia = models.PositiveIntegerField('Existencia', 
		null=False, default=0)

	def __str__(self):
		return self.nombre
	
	class Meta:
		db_table = 'producto'
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'


class DetalleProducto(models.Model):
	producto = models.ForeignKey(
		Producto, on_delete=models.CASCADE, 
		null=False, blank=False, related_name='elproducto')
	numeroloteproducto = models.PositiveIntegerField('Numero de lote del producto',
		null=False, blank=False)
	cantidad = models.PositiveIntegerField('Cantidad', 
		null=False, default=0)
	preciocompra = models.FloatField('Precio del costo', 
		null=False, blank=False, default=0)
	precioventa = models.FloatField('Precio venta',
		null=False, blank=False, default=0)
	fechavencimiento = models.DateField('Fecha de vencimiento',
		null=False, blank=False)
	fechacompra = models.DateField('Fecha de compra', 
		null=True, blank=True)
	ubicacion = models.ForeignKey(
		Ubicacion, on_delete=models.CASCADE, null=False, blank=False)


	
	class Meta():
		db_table = 'detalleproducto'
		verbose_name = 'Detalle producto'
		verbose_name_plural = 'Detalle de productos'








