from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.views.generic import  View, TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Turismo
from .forms import TurismoForm
from Apps.usuarios.mixins import LoginAndSuperStaffMixin
from Apps.usuarios.models import Usuario
from Apps.reservas.models import ReservaHotel, ReservaDeporte, ReservaPlato, ReservaTurismo

# Create your views here.
class AgregarTurismo(LoginAndSuperStaffMixin,CreateView):
	model = Turismo
	form_class = TurismoForm
	template_name = 'turismos/perfil_ModalAgregarTurismo.html'

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			form = self.form_class(data=request.POST,files=request.FILES)
			usuario = Usuario.objects.filter(id = request.user.id)
			print(usuario)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.user_id = request.user
				obj.save()
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
			return redirect('templates_turismo:listar_turismos')

class PerfilListarTurismos(LoginAndSuperStaffMixin, TemplateView):
    template_name = 'turismos/perfil_listarTurismos.html'

    def get_context_data(self, **kwargs):
    	context = super(PerfilListarTurismos, self).get_context_data(**kwargs)
    	context['reserva_deportes'] = ReservaDeporte.objects.all()
    	context['reserva_hoteles'] = ReservaHotel.objects.all()
    	context['reserva_platos'] = ReservaPlato.objects.all()
    	context['reserva_turismos'] = ReservaTurismo.objects.all()
    	return context

class ListarTurismos(LoginAndSuperStaffMixin,ListView):
	model = Turismo

	def get_queryset(self):
		return self.model.objects.all()

	def get(self,request,*args,**kwargs):
		if request.is_ajax():
			return HttpResponse(serialize('json', self.get_queryset()), 'application/json')

		else:
			return redirect('templates_turismo:inicio_turismos')

class TurismoPerfilDetalles(DetailView):
	model = Turismo
	template_name = 'turismos/perfil_ModalTurismoDetalles.html'

class EditarTurismo(LoginAndSuperStaffMixin,UpdateView):
	model = Turismo
	form_class = TurismoForm
	template_name = 'turismos/perfil_ModalEditarTurismo.html'

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
			return redirect('templates_turismo:listar_turismos')

class EliminarTurismo(LoginAndSuperStaffMixin,DeleteView):
	model = Turismo
	template_name = 'turismos/perfil_ModalEliminarTurismo.html'

	def delete(self, request, *args, **kwargs):
		if request.is_ajax():
			deporte = self.get_object()
			deporte.delete()
			mensaje = f'{self.model.__name__} eliminado correctamente!'
			error = 'No hay error!'
			response = JsonResponse({'mensaje':mensaje,'error':error})
			response.status_code = 201
			#retorna response para ser interpretado con javascript
			return response

		else:
			return redirect('templates_turismo:listar_turismos')