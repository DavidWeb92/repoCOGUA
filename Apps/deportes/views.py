import json
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.views.generic import  View, TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from .models import Deporte
from .forms import DeporteForm
from Apps.usuarios.mixins import LoginAndSuperStaffMixin
from Apps.usuarios.models import Usuario
from Apps.reservas.models import ReservaHotel, ReservaDeporte, ReservaPlato, ReservaTurismo
import cloudinary
# Create your views here.

class AgregarDeporte(LoginAndSuperStaffMixin,CreateView):
	model = Deporte
	form_class = DeporteForm
	template_name = 'deportes/perfil_ModalAgregarDeporte.html'

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
			return redirect('templates_deporte:listar_deporte')

'''class ListarDeporte(ListView):
	model = Deporte
	template_name = 'deportes/perfil_listarDeporte.html'
	context_object_name = 'deportes'
	queryset = Deporte.objects.all()'''
class PerfilListarDeportes(LoginAndSuperStaffMixin, TemplateView):
    template_name = 'deportes/perfil_listarDeporte.html'

    def get_context_data(self, **kwargs):
    	context = super(PerfilListarDeportes, self).get_context_data(**kwargs)
    	context['reserva_deportes'] = ReservaDeporte.objects.all()
    	context['reserva_hoteles'] = ReservaHotel.objects.all()
    	context['reserva_platos'] = ReservaPlato.objects.all()
    	context['reserva_turismos'] = ReservaTurismo.objects.all()
    	return context

class ListarDeporte(LoginAndSuperStaffMixin,ListView):
	model = Deporte

	def get_queryset(self):
		return self.model.objects.all()

	#definir una consulta por json que funciona atravez de la consulta de arriba get_queryset en este caso es consulta all
	def get(self,request,*args,**kwargs):
		#json -> forma atuomatica
		if request.is_ajax():
			#serialize-> es una serializacion, convierte una informacion de un tipo a otro, es decir por ejmplo de lista a texto
			#json se retorna atravez de HttpResponse
			return HttpResponse(serialize('json', self.get_queryset()), 'application/json')

		else:
			return redirect('templates_deporte:inicio_deportes')

class DeportePerfilDetalles(DetailView):
	model = Deporte
	template_name = 'deportes/perfil_ModalDeporteDetalles.html'

class EditarDeporte(LoginAndSuperStaffMixin,UpdateView):
	model = Deporte
	form_class = DeporteForm
	template_name = 'deportes/perfil_ModalEditarDeporte.html'

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			form = self.form_class(data=request.POST,files=request.FILES,instance = self.get_object())
			if form.is_valid():
				cloudinary.uploader.destroy(self.get_object().imagen.public_id,invalidate=True)
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
			return redirect('templates_deporte:listar_deporte')

'''def eliminarDeporte(request, id):
	deporte = Deporte.objects.get(id = id)
	deporte.delete()
	return redirect('templates_deporte:listar_deporte')'''

class EliminarDeporte(LoginAndSuperStaffMixin,DeleteView):
	model = Deporte
	template_name = 'deportes/perfil_ModalEliminarDeporte.html'

	def delete(self, request, *args, **kwargs):
		if request.is_ajax():
			cloudinary.uploader.destroy(self.get_object().imagen.public_id,invalidate=True)
			deporte = self.get_object()
			deporte.delete()
			mensaje = f'{self.model.__name__} eliminado correctamente!'
			error = 'No hay error!'
			response = JsonResponse({'mensaje':mensaje,'error':error})
			response.status_code = 201
			#retorna response para ser interpretado con javascript
			return response

		else:
			return redirect('templates_deporte:listar_deporte')