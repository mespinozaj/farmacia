from django.db import models
from apps.persona.models import Persona

# Create your models here.

class Cliente(Persona):
	nit = models.CharField('NIT', null=False, blank=False, 
		max_length=10, unique=True)

	def __str__(self):
		return (self.nombre + ' ' + self.apellido)

	class Meta():
		db_table = 'cliente'
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'





