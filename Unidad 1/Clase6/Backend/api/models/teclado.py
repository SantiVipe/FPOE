from django.db import models
class Teclado(models.Model):
	teclado 			= models.TextField(max_length=50, null=False, blank=True)
	switch				= models.TextField(max_length=5000, null=False, blank=True)
	keycaps 			= models.TextField(max_length=5000, null=False, blank=True)
	formato 			= models.TextField(max_length=5000, null=False, blank=True)
	conectividad 		= models.TextField(max_length=5000, blank=True, unique=True)
	def __str__(self):
		return self.teclado
