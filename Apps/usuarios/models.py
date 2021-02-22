from django.db import models
from django.utils import timezone
from smartfields import fields
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
'''class UsuarioManager(BaseUserManager):
	def create_user(self,email,nombres,apellidos,password=None):
		if not email:
			raise ValueError('El usuario debe tener un correo electrónico')
		usuario = self.model(
			email = self.normalize_email(email),
			nombres = nombres,
			apellidos = apellidos
		)

		usuario.set_password(password)
		usuario.save()
		return usuario

	def create_superuser(self, email, nombres, apellidos, password):
		usuario = self.create_user(
			email,
			nombres = nombres,
			apellidos = apellidos,
			password = password
		)
		usuario.usuario_administrador = True
		usuario.save()
		return usuario'''
class UsuarioManager(BaseUserManager):
	#def _create_user() va a ser llamada cuando utilicemos la consola
	def _create_user(self,email,nombres,apellidos,password,is_staff,is_superuser,**extra_fields):
		user = self.model(
			email = email,
			nombres = nombres,
			apellidos = apellidos,
			is_staff = is_staff,
			is_superuser = is_superuser,
			**extra_fields
		)

		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_user(self,email,nombres,apellidos,password = None,**extra_fields):
		return self._create_user(email,nombres,apellidos,password,False,False,**extra_fields)

	def create_superuser(self,email,nombres,apellidos,password = None,**extra_fields):
		return self._create_user(email,nombres,apellidos,password,True,True,**extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField('Email:', max_length = 254, unique= True)
	nombres = models.CharField('Nombres:', max_length=200, blank = False, null = False)
	apellidos = models.CharField('Apellidos:', max_length=200, blank = False, null = False)
	imagen = fields.ImageField('Imagen', upload_to='imagenes/usuarios/%Y/%m/%d/', max_length=200, blank = True, null = True)
	usuario_activo = models.BooleanField(default = True)
	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)
	created = models.DateTimeField('Fecha de registro', editable=False, null=True,blank=True)
	modified = models.DateTimeField('Ultima modificación', editable=False, null=True, blank=True)

	objects = UsuarioManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nombres', 'apellidos']

	def natural_key(self):
		return f'{self.nombres} {self.apellidos}'

	def __str__(self):
		return f'{self.nombres} {self.apellidos}'

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.modified = timezone.now()
		return super(Usuario, self).save(*args, **kwargs)

	