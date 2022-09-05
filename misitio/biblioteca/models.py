from django.db import models

# Create your models here.
class Editorial(models.Model):
	nombre = models.CharField(max_length=30)
	domicilio = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=60)
	estado = models.CharField(max_length=30)
	pais = models.CharField(max_length=50)
	sitioweb = models.URLField()

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Editoriales"
	
	def __str__(self):
		return "%s" % self.nombre

class Autor(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=40)
	email = models.EmailField(blank=True)

	class Meta:
		verbose_name_plural = "Autores"

	def __str__(self):
		return "%s %s" % (self.nombre, self.apellidos)

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autores = models.ManyToManyField(Autor)
	editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
	fecha_publicacion = models.DateField()
	portada = models.ImageField(upload_to='portadas')

	def __str__(self):
		return "%s" % self.titulo

