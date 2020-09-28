from django.contrib import admin
from .models import *

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
	search_fiels= ['nombre', 'apellido']
	list_filter = ['nombre']
	list_display = ['nombre', 'apellido']


	

admin.site.register(Empleado, EmpleadoAdmin)

# Register your models here.
