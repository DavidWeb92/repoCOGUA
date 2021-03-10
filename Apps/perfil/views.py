from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login, logout, get_user_model
from django.contrib import admin
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from itertools import chain
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  View, TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView
from Apps.usuarios.forms import LoginForm
from django.contrib.auth.forms import PasswordChangeForm

#import para envio de correos d confirmacion
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from Apps.usuarios.tokens import account_activation_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
#fin de import para envio de correos d confirmacion

from Apps.usuarios.models import Usuario
from Apps.usuarios.forms import LoginForm, RegistrarUsuarioForm, EditarUsuarioForm

from Apps.reservas.models import ReservaHotel, ReservaDeporte, ReservaPlato, ReservaTurismo
from Apps.usuarios.mixins import LoginAndSuperStaffMixin

# Create your views here.
#LoginRequiredMixin es otra manera de de proteger nuestra vista
#es decir necesita iniciar sesion para dirgirise al perfil de ussuario
#de esta manera se hace desde las clases y no desde la url como lo hace login_required
class RegistrarUser(CreateView):
    model = Usuario
    form_class = RegistrarUsuarioForm
    template_name = 'perfil/registrar_user.html'
    success_url = reverse_lazy('templates_home:index')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(data=request.POST,files=request.FILES)
            if form.is_valid():
                #form.save()
                # Create an inactive user with no password:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activa tu cuenta de COGUA'
                message = render_to_string('perfil/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
                response.status_code = 201
                return response
                
            else:
                mensaje = f'El registro no se ha podido realizar, porfavor intentelo nuevamente!'
                #guardamos todos los errores mediante form.errors
                error = form.errors
                response = JsonResponse({'mensaje':mensaje,'error':error})
                response.status_code = 400
                return response

        else:
            return redirect('registrar_user')

User = get_user_model()
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return HttpResponseRedirect('/accounts-confirmed/login/')
    else:
        return HttpResponse('El enlace de activación no es válido.')

class EditarUserActual(UpdateView):
	model = Usuario
	form_class = EditarUsuarioForm
	template_name = 'perfil/perfil_user_actual/editar.html'
	success_url = reverse_lazy('templates_perfil:perfil')

	def dispatch(self, request, *args, **kwargs):
		self.objects = self.get_object()
		return super().dispatch(request, *args, **kwargs)

	def get_object(self, queryset=None):
		return self.request.user

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			form = self.form_class(data=request.POST,files=request.FILES,instance = self.get_object())
			if form.is_valid():
				form.save()
				mensaje = f'{self.model.__name__} actualizado correctamente!'
				error = 'No hay error!'
				response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
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
			return redirect('templates_perfil:perfil')

class EditarPasswordUserActual(FormView):
	model = Usuario
	form_class = PasswordChangeForm
	template_name = 'perfil/perfil_user_actual/editar_password.html'
	success_url = reverse_lazy('login')

	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get_form(self, form_class=None):
		form = PasswordChangeForm(user = self.request.user)
		return form

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			form = PasswordChangeForm(user= request.user, data=request.POST)
			if form.is_valid():
				form.save()
				mensaje = f'{self.model.__name__} actualizado correctamente!'
				error = 'No hay error!'
				response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
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
			return redirect('templates_perfil:perfil')

class Login(FormView):
	template_name = 'perfil/login.html'
	form_class = LoginForm
	success_url = reverse_lazy('templates_perfil:perfil')

	@method_decorator(csrf_protect)
	@method_decorator(never_cache)
	def dispatch(self,request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(self.get_success_url())
		else:
			return super(Login,self).dispatch(request, *args, **kwargs)

	def form_valid(self,form):
		login(self.request,form.get_user())
		return super(Login,self).form_valid(form)

#clase para mostrar interfaz de login con mensaje de succeseful de confirmacion de email
class LoginConfirmed(FormView):
    template_name = 'perfil/login_email_confirmed.html'
    form_class = LoginForm
    success_url = reverse_lazy('templates_perfil:perfil')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginConfirmed,self).dispatch(request, *args, **kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(LoginConfirmed,self).form_valid(form)

def logoutUsuario(request):
	logout(request)
	return HttpResponseRedirect('/accounts/login/')

class Perfil(LoginRequiredMixin, TemplateView):
	template_name = 'perfil/perfil_user.html'

	def get_context_data(self, **kwargs):
		context = super(Perfil, self).get_context_data(**kwargs)
		context['reserva_deportes'] = ReservaDeporte.objects.all()
		context['reserva_hoteles'] = ReservaHotel.objects.all()
		context['reserva_platos'] = ReservaPlato.objects.all()
		context['reserva_turismos'] = ReservaTurismo.objects.all()
		context['n_reservaciones'] = ReservaDeporte.objects.filter(usuario = self.request.user).count() + ReservaTurismo.objects.filter(usuario = self.request.user).count() + ReservaPlato.objects.filter(usuario = self.request.user).count() + ReservaHotel.objects.filter(usuario = self.request.user).count()
		return context

'''class PerfilDatos(TemplateView):
	template_name = 'perfil/perfil_datos.html'
	'''
'''Inicio listado de reservas de admin'''
#hoteles
class PerfilListarReservasHotelesAdmin(LoginAndSuperStaffMixin, TemplateView):
    template_name = 'perfil/reservas_admin/hoteles/perfil_listarReservasHoteles.html'

    def get_context_data(self, **kwargs):
    	context = super(PerfilListarReservasHotelesAdmin, self).get_context_data(**kwargs)
    	context['reserva_deportes'] = ReservaDeporte.objects.all()
    	context['reserva_hoteles'] = ReservaHotel.objects.all()
    	context['reserva_platos'] = ReservaPlato.objects.all()
    	context['reserva_turismos'] = ReservaTurismo.objects.all()
    	return context

class ListarReservasHotelesAdmin(LoginAndSuperStaffMixin,ListView):
	model = ReservaHotel
	def get_queryset(self):
		#return self.model.objects.filter(usuario = self.request.user)
		return self.model.objects.all()

	def get(self,request,*args,**kwargs):
		if request.is_ajax():
			return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')

		else:
			return redirect('templates_perfil:inicio_reservas_hoteles')

class HotelPerfilReservaDetallesAdmin(DetailView):
	model = ReservaHotel
	template_name = 'perfil/reservas_admin/hoteles/perfil_ModalReservaHotelDetalles.html'

#deportes
class PerfilListarReservasDeportesAdmin(LoginAndSuperStaffMixin, TemplateView):
    template_name = 'perfil/reservas_admin/deportes/perfil_listarReservasDeportes.html'

    def get_context_data(self, **kwargs):
    	context = super(PerfilListarReservasDeportesAdmin, self).get_context_data(**kwargs)
    	context['reserva_deportes'] = ReservaDeporte.objects.all()
    	context['reserva_hoteles'] = ReservaHotel.objects.all()
    	context['reserva_platos'] = ReservaPlato.objects.all()
    	context['reserva_turismos'] = ReservaTurismo.objects.all()
    	return context

class ListarReservasDeportesAdmin(LoginAndSuperStaffMixin,ListView):
	model = ReservaDeporte

	def get_queryset(self):
		#return self.model.objects.filter(usuario = self.request.user)
		return self.model.objects.all()

	def get(self,request,*args,**kwargs):
		if request.is_ajax():
			return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')

		else:
			return redirect('templates_perfil:inicio_reservas_deportes')

class DeportePerfilReservaDetallesAdmin(DetailView):
	model = ReservaDeporte
	template_name = 'perfil/reservas_admin/deportes/perfil_ModalReservaDeporteDetalles.html'

#platos tipicos
class PerfilListarReservasPlatosAdmin(LoginAndSuperStaffMixin, TemplateView):
    template_name = 'perfil/reservas_admin/platos/perfil_listarReservasPlatos.html'

    def get_context_data(self, **kwargs):
    	context = super(PerfilListarReservasPlatosAdmin, self).get_context_data(**kwargs)
    	context['reserva_deportes'] = ReservaDeporte.objects.all()
    	context['reserva_hoteles'] = ReservaHotel.objects.all()
    	context['reserva_platos'] = ReservaPlato.objects.all()
    	context['reserva_turismos'] = ReservaTurismo.objects.all()
    	return context

class ListarReservasPlatosAdmin(LoginAndSuperStaffMixin,ListView):
	model = ReservaPlato
	def get_queryset(self):
		#return self.model.objects.filter(usuario = self.request.user)
		return self.model.objects.all()

	def get(self,request,*args,**kwargs):
		if request.is_ajax():
			return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')

		else:
			return redirect('templates_perfil:inicio_reservas_platos')

class PlatoPerfilReservaDetallesAdmin(DetailView):
	model = ReservaPlato
	template_name = 'perfil/reservas_admin/platos/perfil_ModalReservaPlatoDetalles.html'

#Lugares turísticos
class PerfilListarReservasTurismosAdmin(LoginAndSuperStaffMixin, TemplateView):
    template_name = 'perfil/reservas_admin/turismos/perfil_listarReservasTurismos.html'

    def get_context_data(self, **kwargs):
    	context = super(PerfilListarReservasTurismosAdmin, self).get_context_data(**kwargs)
    	context['reserva_deportes'] = ReservaDeporte.objects.all()
    	context['reserva_hoteles'] = ReservaHotel.objects.all()
    	context['reserva_platos'] = ReservaPlato.objects.all()
    	context['reserva_turismos'] = ReservaTurismo.objects.all()
    	return context

class ListarReservasTurismosAdmin(LoginAndSuperStaffMixin,ListView):
	model = ReservaTurismo
	def get_queryset(self):
		#return self.model.objects.filter(usuario = self.request.user)
		return self.model.objects.all()

	def get(self,request,*args,**kwargs):
		if request.is_ajax():
			return HttpResponse(serialize('json', self.get_queryset(),use_natural_foreign_keys = True), 'application/json')

		else:
			return redirect('templates_perfil:inicio_reservas_turismos')

class TurismoPerfilReservaDetallesAdmin(DetailView):
	model = ReservaTurismo
	template_name = 'perfil/reservas_admin/turismos/perfil_ModalReservaTurismoDetalles.html'

'''Fin listado de reservas de admin'''

'''Inicio listado de reservas de Usuarios'''
#all
import itertools 
class ListarReservasUser(LoginRequiredMixin,ListView):
	model1 = ReservaDeporte
	model2 = ReservaTurismo
	model3 = ReservaPlato
	model4 = ReservaHotel

	paginate_by = 3
	template_name = 'perfil/reservas_user/perfil_listarReservasUser.html'

	def get_queryset(self):
		queryset1 = ReservaDeporte.objects.filter(usuario = self.request.user)
		queryset2 = ReservaTurismo.objects.filter(usuario = self.request.user)
		queryset3 = ReservaPlato.objects.filter(usuario = self.request.user)
		queryset4 = ReservaHotel.objects.filter(usuario = self.request.user)
		return list(itertools.chain(queryset1, queryset2, queryset3, queryset4))

	def get_context_data(self, **kwargs):
		context = super(ListarReservasUser, self).get_context_data(**kwargs)
		context['reserva_deportes_user'] = ReservaDeporte.objects.filter(usuario = self.request.user)
		context['reserva_turismos_user'] = ReservaTurismo.objects.filter(usuario = self.request.user)
		context['reserva_platos_user'] = ReservaPlato.objects.filter(usuario = self.request.user)
		context['reserva_hoteles_user'] = ReservaHotel.objects.filter(usuario = self.request.user)
		context['n_reservaciones'] = ReservaDeporte.objects.filter(usuario = self.request.user).count() + ReservaTurismo.objects.filter(usuario = self.request.user).count() + ReservaPlato.objects.filter(usuario = self.request.user).count() + ReservaHotel.objects.filter(usuario = self.request.user).count()
		return context

class DeportePerfilReservaDetallesUser(LoginRequiredMixin, DetailView):
	model = ReservaDeporte
	template_name = 'perfil/reservas_user/deportes/perfil_ModalReservaDeporteDetalles.html'
'''Fin listado de reservas de Usuarios'''