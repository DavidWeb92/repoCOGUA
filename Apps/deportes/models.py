from django.db import models
from django.utils import timezone
from Apps.usuarios.models import Usuario
from smartfields import fields
from cloudinary.models import CloudinaryField
# Create your models here.
class Deporte(models.Model):
	nombre = models.CharField(max_length = 200, blank = False, null = False)
	precio = models.CharField('Precio',max_length = 200, blank = False, null = False)
	descripcion = models.TextField('Descripcion',blank=True, null=True)
	#estado = models.BooleanField('No Reservado/Reservado',default = False)
	cantidad = models.SmallIntegerField('Cantidad', default = 1)
	imagen = CloudinaryField('Imagen',folder = "Deportes/")
	#fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
	user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE,blank = True,null = True)
	created = models.DateTimeField('Fecha de publicacion', editable=False, null=True,blank=True)
	modified = models.DateTimeField('Fecha de modificacion', editable=False, null=True, blank=True)

	def natural_key(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Deporte, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Deporte'
		verbose_name_plural = 'Deportes'
		#ordering -> ordena por nombre alfabeticamente
		ordering = ['nombre']

	def __str__(self):
		return '{}'.format(self.nombre)