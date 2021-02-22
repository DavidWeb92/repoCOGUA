#un json no es una lista es un texto
#para ello debemos importar json
#Inicio importaciones principales para peticiones con ajax
import json
from django.core.serializers import serialize
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
#fin importaciones principales para peticiones con ajax
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, DetailView
from Apps.usuarios.models import Usuario
from .forms import LoginForm, RegistrarUsuarioForm, EditarUsuarioForm, EditarPasswordUsuarioForm
from Apps.usuarios.mixins import LoginAndSuperStaffMixin, PermisosUsuariosMixin
from Apps.reservas.models import ReservaHotel, ReservaDeporte, ReservaPlato, ReservaTurismo

# Create your views here.
'''class RegistrarUsuario(CreateView):
	model = Usuario
	form_class = RegistrarUsuarioForm
	template_name = 'usuarios/registrar_usuario.html'
	success_url = reverse_lazy('templates_usuario:listar_usuario')'''

#Registro de usuario usando cleaned_data
class RegistrarUsuario(PermisosUsuariosMixin,LoginAndSuperStaffMixin,CreateView):
	model = Usuario
	form_class = RegistrarUsuarioForm
	template_name = 'usuarios/perfil_ModalAgregarUsuario.html'

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			form = self.form_class(data=request.POST,files=request.FILES)
			if form.is_valid():
				form.save()
				mensaje = f'{self.model.__name__} registrado correctamente!'
				error = 'No hay error!'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 201
				#retorna response para ser interpretado con javascript
				return response

			else:
				mensaje = f'El {self.model.__name__} no se ha podido registrar, porfavor intentelo nuevamente!'
				#guardamos todos los errores mediante form.errors
				error = form.errors
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

		else:
			return redirect('templates_usuario:listar_usuario')
class PerfilListarUsuario(PermisosUsuariosMixin,LoginAndSuperStaffMixin, TemplateView):
    template_name = 'usuarios/perfil_listarUsuarios.html'

    def get_context_data(self, **kwargs):
    	context = super(PerfilListarUsuario, self).get_context_data(**kwargs)
    	context['reserva_deportes'] = ReservaDeporte.objects.all()
    	context['reserva_hoteles'] = ReservaHotel.objects.all()
    	context['reserva_platos'] = ReservaPlato.objects.all()
    	context['reserva_turismos'] = ReservaTurismo.objects.all()
    	return context

class ListarUsuario(PermisosUsuariosMixin,LoginAndSuperStaffMixin,ListView):
	model = Usuario

	def get_queryset(self):
		return self.model.objects.all()

	def get(self,request,*args,**kwargs):
		if request.is_ajax():
			return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
		else:
			return redirect('templates_usuario:inicio_usuarios')
class UsuarioPerfilDetalles(DetailView):
	model = Usuario
	template_name = 'usuarios/perfil_ModalUsuarioDetalles.html'

class EditarUsuario(PermisosUsuariosMixin,LoginAndSuperStaffMixin, UpdateView):
	model = Usuario
	form_class = EditarUsuarioForm
	template_name = 'usuarios/perfil_ModalEditarUsuario.html'

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			form = self.form_class(data=request.POST,files=request.FILES,instance = self.get_object())
			if form.is_valid():
				form.save()
				mensaje = f'{self.model.__name__} actualizado correctamente!'
				error = 'No hay error!'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 201
				#retorna response para ser interpretado con javascript
				return response

			else:
				mensaje = f'El {self.model.__name__} no se ha podido actualizar, porfavor intentelo nuevamente!'
				#guardamos todos los errores mediante form.errors
				error = form.errors
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

		else:
			return redirect('templates_usuario:listar_usuario')

class EditarUsuarioPassword(PermisosUsuariosMixin,LoginAndSuperStaffMixin, UpdateView):
	model = Usuario
	form_class = EditarPasswordUsuarioForm
	template_name = 'usuarios/perfil_ModalEditarPasswordUsuario.html'

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			form = self.form_class(request.POST,instance = self.get_object())
			if form.is_valid():
				form.save()
				mensaje = f'{self.model.__name__} actualizado correctamente!'
				error = 'No hay error!'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 201
				#retorna response para ser interpretado con javascript
				return response

			else:
				mensaje = f'El {self.model.__name__} no se ha podido actualizar, porfavor intentelo nuevamente!'
				#guardamos todos los errores mediante form.errors
				error = form.errors
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

		else:
			return redirect('templates_usuario:listar_usuario')

class EliminarUsuario(PermisosUsuariosMixin,LoginAndSuperStaffMixin, DeleteView):
	model = Usuario
	template_name = 'usuarios/perfil_ModalEliminarUsuario.html'

	def delete(self, request, *args, **kwargs):
		if request.is_ajax():
			usuario = self.get_object()
			if usuario.is_superuser == True:
				mensaje = f'El {self.model.__name__} es un Super User. Si desea eliminar este usuario, debe realizar esta acción desde el panel de Administración de Cogua'
				error = 'Existe error!'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				#retorna response para ser interpretado con javascript
				return response
			else:
				usuario.delete()
				mensaje = f'{self.model.__name__} eliminado correctamente!'
				error = 'No hay error!'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 201
				#retorna response para ser interpretado con javascript
				return response

		else:
			return redirect('templates_usuario:listar_usuario')