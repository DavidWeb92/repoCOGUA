from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from datetime import date, datetime 
from Apps.reservas.models import ReservaDeporte, ReservaHotel, ReservaPlato, ReservaTurismo
from Apps.usuarios.models import Usuario
from Apps.deportes.models import Deporte
from Apps.hoteles.models import Hotel
from Apps.platos.models import Plato
from Apps.turismos.models import Turismo
from .forms import ReservaDeporteForm, ReservaHotelForm

# Create your views here.
primer_error_else = f'La reserva no se ha podido realizar, los campos de fechas aún están vacíos !'
segundo_error_else = f'La reserva no se ha podido realizar. El campo de fecha de inicio aun esta vacio !'
tercer_error_else = f'La reserva no se ha podido realizar. el campo de fecha de fin aun esta vacio !'
cuarto_error_else = f'La reserva no se ha podido realizar. La fecha de inicio no puede ser el mismo dia o los dias anteriores que la fecha de hoy !!'
quinto_error_else = f'La reserva no se ha podido realizar. La fecha de fin no puede ser el mismo dia o los dias anteriores que la fecha de hoy !!'
sexto_error_else = f'La reserva no se ha podido realizar. La fecha de fin es menor que la fecha de inicio !'
septimo_error_else = f'La reserva no se ha podido realizar. La fecha de inicio no puede ser el mismo dia o los dias anteriores que la fecha de hoy !!'
octavo_error_else = f'La reserva no se ha podido realizar. La fecha de fin no puede ser el mismo dia o los dias anteriores que la fecha de hoy !!'

class ReservaDeporteDetalles(DetailView):
	model = Deporte
	template_name = 'home/deportes/index_ModalReservarDeporte.html'

class RegistrarReservaDeporte(CreateView):
	model = ReservaDeporte
	success_url = reverse_lazy('templates_home:listado_deportes_disponibles')

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			usuario = Usuario.objects.filter(id = request.POST.get('usuario')).first()
			deporte = Deporte.objects.filter(id = request.POST.get('deporte')).first()
			fecha_inicial = request.POST.get('fecha1')
			fecha_final = request.POST.get('fecha2')
			fecha_actual = datetime.today();
				
			if fecha_inicial and fecha_final:
				#datetime.strptime(fecha_inicial, '%Y-%m-%d') -> permite transformar un string a date
				fecha_inicial_a_date = datetime.strptime(fecha_inicial, '%Y-%m-%d')
				fecha_final_a_date = datetime.strptime(fecha_final, '%Y-%m-%d')

				if fecha_inicial_a_date > fecha_actual and fecha_final_a_date > fecha_actual and fecha_final_a_date > fecha_inicial_a_date or fecha_final_a_date == fecha_inicial_a_date:
					if fecha_final_a_date == fecha_inicial_a_date:
						if fecha_inicial_a_date > fecha_actual and fecha_final_a_date > fecha_actual:
							nueva_reserva = self.model(
								usuario = usuario,
								deporte = deporte,
								fecha_inicial = fecha_inicial,
								fecha_final = fecha_final
							)
							nueva_reserva.save()
							mensaje = f'{self.model.__name__} registrado correctamente!'
							error = 'No hay error!'
							response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
							response.status_code = 201
							return response

						# septimo error else
						elif fecha_inicial_a_date < fecha_actual:
							mensaje = septimo_error_else
							error = 'necesita rellenar el campo'
							response = JsonResponse({'mensaje':mensaje,'error':error})
							response.status_code = 400
							return response

						# octavo error else
						elif fecha_final_a_date < fecha_actual:
							mensaje = octavo_error_else
							error = 'necesita rellenar el campo'
							response = JsonResponse({'mensaje':mensaje,'error':error})
							response.status_code = 400
							return response

					else:
						nueva_reserva = self.model(
							usuario = usuario,
							deporte = deporte,
							fecha_inicial = fecha_inicial,
							fecha_final = fecha_final
						)
						nueva_reserva.save()
						mensaje = f'{self.model.__name__} registrado correctamente!'
						error = 'No hay error!'
						response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
						response.status_code = 201
						return response

				# cuarto error else
				elif fecha_inicial_a_date < fecha_actual:
					mensaje = cuarto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

				# quinto error else
				elif fecha_final_a_date < fecha_actual:
					mensaje = quinto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

				# sexto error else
				elif fecha_final_a_date < fecha_inicial_a_date:
					mensaje = sexto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

			# primer error else
			elif not fecha_inicial and not fecha_final:
				mensaje = primer_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

			# segundo error else
			elif not fecha_inicial:
				mensaje = segundo_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

			# tercer error else
			elif not fecha_final:
				mensaje = tercer_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response
		return redirect('templates_home:listado_deportes_disponibles')

class EliminarReservaDeporte(DeleteView):
	model = ReservaDeporte

	def delete(self, request, *args, **kwargs):
		if request.is_ajax():
			reservadeporte = self.get_object()
			reservadeporte.delete()
			mensaje = f'{self.model.__name__} eliminado correctamente!'
			error = 'No hay error!'
			response = JsonResponse({'mensaje':mensaje,'error':error})
			response.status_code = 201
			#retorna response para ser interpretado con javascript
			return response

		else:
			return redirect('templates_perfil:listar_reservas_deportes')

class ReservaHotelDetalles(DetailView):
	model = Hotel
	template_name = 'home/hoteles/index_ModalReservarHotel.html'

class RegistrarReservaHotel(CreateView):
	model = ReservaHotel
	success_url = reverse_lazy('templates_home:listado_hoteles_disponibles')

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			usuario = Usuario.objects.filter(id = request.POST.get('usuario')).first()
			hotel = Hotel.objects.filter(id = request.POST.get('hotel')).first()
			fecha_inicial = request.POST.get('fecha1')
			fecha_final = request.POST.get('fecha2')
			fecha_actual = datetime.today();
				
			if fecha_inicial and fecha_final:
				#datetime.strptime(fecha_inicial, '%Y-%m-%d') -> permite transformar un string a date
				fecha_inicial_a_date = datetime.strptime(fecha_inicial, '%Y-%m-%d')
				fecha_final_a_date = datetime.strptime(fecha_final, '%Y-%m-%d')

				if fecha_inicial_a_date > fecha_actual and fecha_final_a_date > fecha_actual and fecha_final_a_date > fecha_inicial_a_date or fecha_final_a_date == fecha_inicial_a_date:
					if fecha_final_a_date == fecha_inicial_a_date:
						if fecha_inicial_a_date > fecha_actual and fecha_final_a_date > fecha_actual:
							nueva_reserva = self.model(
								usuario = usuario,
								hotel = hotel,
								fecha_inicial = fecha_inicial,
								fecha_final = fecha_final
							)
							nueva_reserva.save()
							mensaje = f'{self.model.__name__} registrado correctamente!'
							error = 'No hay error!'
							response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
							response.status_code = 201
							return response

						# septimo error else
						elif fecha_inicial_a_date < fecha_actual:
							mensaje = septimo_error_else
							error = 'necesita rellenar el campo'
							response = JsonResponse({'mensaje':mensaje,'error':error})
							response.status_code = 400
							return response

						# octavo error else
						elif fecha_final_a_date < fecha_actual:
							mensaje = octavo_error_else
							error = 'necesita rellenar el campo'
							response = JsonResponse({'mensaje':mensaje,'error':error})
							response.status_code = 400
							return response

					else:
						nueva_reserva = self.model(
							usuario = usuario,
							hotel = hotel,
							fecha_inicial = fecha_inicial,
							fecha_final = fecha_final
						)
						nueva_reserva.save()
						mensaje = f'{self.model.__name__} registrado correctamente!'
						error = 'No hay error!'
						response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
						response.status_code = 201
						return response

				# cuarto error else
				elif fecha_inicial_a_date < fecha_actual:
					mensaje = cuarto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

				# quinto error else
				elif fecha_final_a_date < fecha_actual:
					mensaje = quinto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

				# sexto error else
				elif fecha_final_a_date < fecha_inicial_a_date:
					mensaje = sexto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

			# primer error else
			elif not fecha_inicial and not fecha_final:
				mensaje = primer_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

			# segundo error else
			elif not fecha_inicial:
				mensaje = segundo_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

			# tercer error else
			elif not fecha_final:
				mensaje = tercer_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

		return redirect('templates_home:listado_hoteles_disponibles')

class EliminarReservaHotel(DeleteView):
	model = ReservaHotel

	def delete(self, request, *args, **kwargs):
		if request.is_ajax():
			reservahotel = self.get_object()
			reservahotel.delete()
			mensaje = f'{self.model.__name__} eliminado correctamente!'
			error = 'No hay error!'
			response = JsonResponse({'mensaje':mensaje,'error':error})
			response.status_code = 201
			#retorna response para ser interpretado con javascript
			return response

		else:
			return redirect('templates_perfil:listar_reservas_hoteles')

class ReservaPlatoDetalles(DetailView):
	model = Plato
	template_name = 'home/platos/index_ModalReservarPlato.html'

class RegistrarReservaPlato(CreateView):
	model = ReservaPlato
	success_url = reverse_lazy('templates_home:listado_platos_disponibles')

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			usuario = Usuario.objects.filter(id = request.POST.get('usuario')).first()
			plato = Plato.objects.filter(id = request.POST.get('plato')).first()
			fecha_inicial = request.POST.get('fecha1')
			fecha_final = request.POST.get('fecha2')
			fecha_actual = datetime.today();
				
			if fecha_inicial and fecha_final:
				#datetime.strptime(fecha_inicial, '%Y-%m-%d') -> permite transformar un string a date
				fecha_inicial_a_date = datetime.strptime(fecha_inicial, '%Y-%m-%d')
				fecha_final_a_date = datetime.strptime(fecha_final, '%Y-%m-%d')

				if fecha_inicial_a_date > fecha_actual and fecha_final_a_date > fecha_actual and fecha_final_a_date > fecha_inicial_a_date or fecha_final_a_date == fecha_inicial_a_date:
					if fecha_final_a_date == fecha_inicial_a_date:
						if fecha_inicial_a_date > fecha_actual and fecha_final_a_date > fecha_actual:
							nueva_reserva = self.model(
								usuario = usuario,
								plato = plato,
								fecha_inicial = fecha_inicial,
								fecha_final = fecha_final
							)
							nueva_reserva.save()
							mensaje = f'{self.model.__name__} registrado correctamente!'
							error = 'No hay error!'
							response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
							response.status_code = 201
							return response

						# septimo error else
						elif fecha_inicial_a_date < fecha_actual:
							mensaje = septimo_error_else
							error = 'necesita rellenar el campo'
							response = JsonResponse({'mensaje':mensaje,'error':error})
							response.status_code = 400
							return response

						# octavo error else
						elif fecha_final_a_date < fecha_actual:
							mensaje = octavo_error_else
							error = 'necesita rellenar el campo'
							response = JsonResponse({'mensaje':mensaje,'error':error})
							response.status_code = 400
							return response

					else:
						nueva_reserva = self.model(
							usuario = usuario,
							plato = plato,
							fecha_inicial = fecha_inicial,
							fecha_final = fecha_final
						)
						nueva_reserva.save()
						mensaje = f'{self.model.__name__} registrado correctamente!'
						error = 'No hay error!'
						response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
						response.status_code = 201
						return response

				# cuarto error else
				elif fecha_inicial_a_date < fecha_actual:
					mensaje = cuarto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

				# quinto error else
				elif fecha_final_a_date < fecha_actual:
					mensaje = quinto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

				# sexto error else
				elif fecha_final_a_date < fecha_inicial_a_date:
					mensaje = sexto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

			# primer error else
			elif not fecha_inicial and not fecha_final:
				mensaje = primer_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

			# segundo error else
			elif not fecha_inicial:
				mensaje = segundo_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

			# tercer error else
			elif not fecha_final:
				mensaje = tercer_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

		return redirect('templates_home:listado_platos_disponibles')

class EliminarReservaPlato(DeleteView):
	model = ReservaPlato

	def delete(self, request, *args, **kwargs):
		if request.is_ajax():
			reservahotel = self.get_object()
			reservahotel.delete()
			mensaje = f'{self.model.__name__} eliminado correctamente!'
			error = 'No hay error!'
			response = JsonResponse({'mensaje':mensaje,'error':error})
			response.status_code = 201
			#retorna response para ser interpretado con javascript
			return response

		else:
			return redirect('templates_perfil:listar_reservas_platos')

class ReservaTurismoDetalles(DetailView):
	model = Turismo
	template_name = 'home/turismos/index_ModalReservarTurismo.html'

class RegistrarReservaTurismo(CreateView):
	model = ReservaTurismo
	success_url = reverse_lazy('templates_home:listado_turismos_disponibles')

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			usuario = Usuario.objects.filter(id = request.POST.get('usuario')).first()
			turismo = Turismo.objects.filter(id = request.POST.get('turismo')).first()
			fecha_inicial = request.POST.get('fecha1')
			fecha_final = request.POST.get('fecha2')
			fecha_actual = datetime.today();
				
			if fecha_inicial and fecha_final:
				#datetime.strptime(fecha_inicial, '%Y-%m-%d') -> permite transformar un string a date
				fecha_inicial_a_date = datetime.strptime(fecha_inicial, '%Y-%m-%d')
				fecha_final_a_date = datetime.strptime(fecha_final, '%Y-%m-%d')

				if fecha_inicial_a_date > fecha_actual and fecha_final_a_date > fecha_actual and fecha_final_a_date > fecha_inicial_a_date or fecha_final_a_date == fecha_inicial_a_date:
					if fecha_final_a_date == fecha_inicial_a_date:
						if fecha_inicial_a_date > fecha_actual and fecha_final_a_date > fecha_actual:
							nueva_reserva = self.model(
								usuario = usuario,
								turismo = turismo,
								fecha_inicial = fecha_inicial,
								fecha_final = fecha_final
							)
							nueva_reserva.save()
							mensaje = f'{self.model.__name__} registrado correctamente!'
							error = 'No hay error!'
							response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
							response.status_code = 201
							return response

						# septimo error else
						elif fecha_inicial_a_date < fecha_actual:
							mensaje = septimo_error_else
							error = 'necesita rellenar el campo'
							response = JsonResponse({'mensaje':mensaje,'error':error})
							response.status_code = 400
							return response

						# octavo error else
						elif fecha_final_a_date < fecha_actual:
							mensaje = octavo_error_else
							error = 'necesita rellenar el campo'
							response = JsonResponse({'mensaje':mensaje,'error':error})
							response.status_code = 400
							return response

					else:
						nueva_reserva = self.model(
							usuario = usuario,
							turismo = turismo,
							fecha_inicial = fecha_inicial,
							fecha_final = fecha_final
						)
						nueva_reserva.save()
						mensaje = f'{self.model.__name__} registrado correctamente!'
						error = 'No hay error!'
						response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
						response.status_code = 201
						return response

				# cuarto error else
				elif fecha_inicial_a_date < fecha_actual:
					mensaje = cuarto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

				# quinto error else
				elif fecha_final_a_date < fecha_actual:
					mensaje = quinto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

				# sexto error else
				elif fecha_final_a_date < fecha_inicial_a_date:
					mensaje = sexto_error_else
					error = 'necesita rellenar el campo'
					response = JsonResponse({'mensaje':mensaje,'error':error})
					response.status_code = 400
					return response

			# primer error else
			elif not fecha_inicial and not fecha_final:
				mensaje = primer_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

			# segundo error else
			elif not fecha_inicial:
				mensaje = segundo_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

			# tercer error else
			elif not fecha_final:
				mensaje = tercer_error_else
				error = 'necesita rellenar el campo'
				response = JsonResponse({'mensaje':mensaje,'error':error})
				response.status_code = 400
				return response

		return redirect('templates_home:listado_turismos_disponibles')

class EliminarReservaTurismo(DeleteView):
	model = ReservaTurismo

	def delete(self, request, *args, **kwargs):
		if request.is_ajax():
			reservahotel = self.get_object()
			reservahotel.delete()
			mensaje = f'{self.model.__name__} eliminado correctamente!'
			error = 'No hay error!'
			response = JsonResponse({'mensaje':mensaje,'error':error})
			response.status_code = 201
			#retorna response para ser interpretado con javascript
			return response

		else:
			return redirect('templates_perfil:listar_reservas_turismos')