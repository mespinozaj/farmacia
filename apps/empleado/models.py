from django.db import models
from apps.persona.models import Persona
from django.contrib.auth.models import User

# Create your models here.

class Empleado(Persona):

	Empleado = models.OneToOneField(User, on_delete=models.CASCADE, default='')
	sueldo = models.IntegerField('Sueldo', null=False, blank=False, default=0)
	
	def __str__(self):
		return self.nombre

	class Meta():
		db_table = 'empleado'
		verbose_name = 'Empleado'
		verbose_name_plural = 'Empleados'
# Create your models here.

	
