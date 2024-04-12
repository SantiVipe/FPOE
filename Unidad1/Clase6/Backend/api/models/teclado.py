from django.db import models
class Teclado():
	teclado 			= models.CharField(max_length=50, null=False, blank=True)
	swtich				= models.TextField(max_length=5000, null=False, blank=True)
	keycaps 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	formato 			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	conectividad 		= models.SlugField(blank=True, unique=True)
	def __str__(self):
		return self.teclado