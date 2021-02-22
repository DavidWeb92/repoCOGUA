from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from Apps.deportes.models import Deporte
from Apps.hoteles.models import Hotel
from Apps.platos.models import Plato
from Apps.turismos.models import Turismo
from Apps.usuarios.models import Usuario

# Modelo de reserva para deportes
class ReservaDeporte(models.Model):
	deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE, verbose_name = "Deporte reservado")
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name = "Reservado por")
	fecha_inicial = models.DateField('Fecha inicial de reserva', blank = False, null = False)
	fecha_final = models.DateField('Fecha final de reserva', blank = False, null = False)
	cantidad_dias = models.SmallIntegerField('Cantidad de dias a reservar', default = 7)
	created = models.DateTimeField('Creado', editable=False, null=True,blank=True)
	modified = models.DateTimeField('Modificado', editable=False, null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(ReservaDeporte, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Deportes reservados'
		verbose_name = 'la reserva'
	def __str__(self):
		return '{}'.format(self.usuario)


def reducir_cantidad_deporte(sender, instance, **kwargs):
	deporte = instance.deporte
	if deporte.cantidad > 0:
		deporte.cantidad = deporte.cantidad - 1
		deporte.save()

post_save.connect(reducir_cantidad_deporte,sender = ReservaDeporte)

# Modelo de reserva para platos tipicos
class ReservaHotel(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name = "Cabaña reservado")
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name = "Reservado por")
	fecha_inicial = models.DateField('Fecha inicial de reserva', blank = False, null = False)
	fecha_final = models.DateField('Fecha final de reserva', blank = False, null = False)
	cantidad_dias = models.SmallIntegerField('Cantidad de dias a reservar', default = 7)
	created = models.DateTimeField('Fecha de publicacion', editable=False, null=True,blank=True)
	modified = models.DateTimeField('Fecha de modificacion', editable=False, null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(ReservaHotel, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Cabañas reservados'
		verbose_name = 'la reserva'
	def __str__(self):
		return '{}'.format(self.usuario)

# Modelo de reserva para platos tipicos
class ReservaPlato(models.Model):
	plato = models.ForeignKey(Plato, on_delete=models.CASCADE, verbose_name = "Plato Tipico reservado")
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name = "Reservado por")
	fecha_inicial = models.DateField('Fecha inicial de reserva', blank = False, null = False)
	fecha_final = models.DateField('Fecha final de reserva', blank = False, null = False)
	cantidad_dias = models.SmallIntegerField('Cantidad de dias a reservar', default = 7)
	created = models.DateTimeField('Fecha de publicacion', editable=False, null=True,blank=True)
	modified = models.DateTimeField('Fecha de modificacion', editable=False, null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(ReservaPlato, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Platos Tipicos reservados'
		verbose_name = 'la reserva'
	def __str__(self):
		return '{}'.format(self.usuario)

# Modelo de reserva para lugares turisticos
class ReservaTurismo(models.Model):
	turismo = models.ForeignKey(Turismo, on_delete=models.CASCADE, verbose_name = "Lugar Turistico reservado")
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name = "Reservado por")
	fecha_inicial = models.DateField('Fecha inicial de reserva', blank = False, null = False)
	fecha_final = models.DateField('Fecha final de reserva', blank = False, null = False)
	cantidad_dias = models.SmallIntegerField('Cantidad de dias a reservar', default = 7)
	created = models.DateTimeField('Fecha de publicacion', editable=False, null=True,blank=True)
	modified = models.DateTimeField('Fecha de modificacion', editable=False, null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(ReservaTurismo, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Lugares turisticos reservados'
		verbose_name = 'la reserva'
	def __str__(self):
		return '{}'.format(self.usuario)