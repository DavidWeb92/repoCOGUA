#archivo creado manualmente
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
#clase que valida si un usuario es un superusuario y tambien siesque a iniciado sesion
class LoginAndSuperStaffMixin(object):
	def dispatch(self, request, *args, **kwargs):
		#primero verifica si a iniciado sesion
		if request.user.is_authenticated:
			# segundo -> is_staff verifica si el ussuario es staf
			if request.user.is_staff:
				return super().dispatch(request, *args, **kwargs)

		return redirect('templates_perfil:perfil')

class PermisosUsuariosMixin(object):
	permission_required = ''
	url_redirect = None

	def get_perms(self):
		if isinstance(self.permission_required,str):
			return (self.permission_required)

		else:
			return self.permission_required

	def get_url_redirect(self):
		if self.url_redirect is None:
			return reverse_lazy('login')
		return self.url_redirect

	def dispatch(self, request, *args, **kwargs):
		if request.user.has_perms(self.get_perms()):
			return super().dispatch(request, *args, **kwargs)
		messages.error(request, 'No tienes permisos para realizar esta accion.')
		return redirect(self.get_url_redirect())