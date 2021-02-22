from django.db import models
from django.utils import timezone
from Apps.usuarios.models import Usuario
from smartfields import fields
# Create your models here.

class Plato(models.Model):
	nombre = models.CharField(max_length = 200, blank = False, null = False)
	precio = models.CharField('Precio',max_length = 200, blank = False, null = False)
	descripcion = models.TextField('Descripcion',blank=False, null=False)
	cantidad = models.SmallIntegerField('Cantidad', default = 1)
	estado = models.BooleanField('Estado',default = False)
	imagen = fields.ImageField('Imagen', upload_to='imagenes/platos_tipicos/%Y/%m/%d/', max_length=200, blank = True, null = True)
	user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE,blank = True,null = True)
	created = models.DateTimeField('Fecha de publicacion', editable=False, null=True,blank=True)
	modified = models.DateTimeField('Fecha de modificacion', editable=False, null=True, blank=True)

	def natural_key(self):
		return self.nombre
		
	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Plato, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Plato'
		verbose_name_plural = 'Platos Tipicos'
		#ordering -> ordena por nombre alfabeticamente
		ordering = ['nombre']

	def __str__(self):
		return '{}'.format(self.nombre)