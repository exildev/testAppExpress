from django.db import models
from django.contrib.auth.models import User

class Motorizado(User):

	nombre = models.CharField(max_length=50)
	identificador = models.CharField(max_length=50)
	tipo = models.IntegerField(choices=((1, 'suscrito'),(2, 'empleado')))
	empresa = models.IntegerField()

	class Meta:
		verbose_name = "Motorizado"
		verbose_name_plural = "Motorizados"
	#end def

	def __str__(self):
		return self.nombre
	#end def

#end class

class Confirmacion(models.Model):
	pedido = models.IntegerField()
	motorizado = models.IntegerField()
	fecha = models.DateTimeField(auto_now=True)
	imagen = models.ImageField()

	class Meta:
		verbose_name = "Confirmacion"
		verbose_name_plural = "Confirmaciones"
	#end def
	def __str__(self):
		return str(self.pedido)
	#end def
#end class