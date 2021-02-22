#archivo creado manualmente
from django.urls import path
from .views import *
#from .views import Perfil,PerfilListarReservasDeportesAdmin,  ListarReservasDeportesAdmin, DeportePerfilReservaDetallesAdmin
#from .views import PerfilListarReservasHotelesAdmin,  ListarReservasHotelesAdmin, HotelPerfilReservaDetallesAdmin
#from .views import PerfilListarReservasPlatosAdmin,  ListarReservasPlatosAdmin, PlatoPerfilReservaDetallesAdmin
#from .views import PerfilListarReservasTurismosAdmin,  ListarReservasTurismosAdmin, TurismoPerfilReservaDetallesAdmin
#from .views import ListarReservasDeportesUser, DeportePerfilReservaDetallesUser
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('perfil/',Perfil.as_view(), name='perfil'),
	#url para editar ussuario actual
	path('perfil/editar_perfil/', EditarUserActual.as_view(), name='editar_perfil_actual'),
	path('perfil/editar_password_perfil/', EditarPasswordUserActual.as_view(), name='editar_perfil_password_actual'),
	#urls para mostrar reservas de user como admin en perfil
	path('perfil_admin/reservas/deportes/',PerfilListarReservasDeportesAdmin.as_view(), name='inicio_reservas_deportes'),
	path('perfil_admin/listar_reservas_deportes/', ListarReservasDeportesAdmin.as_view(), name = 'listar_reservas_deportes'),
	path('perfil_admin/reserva_detalles_deporte/<int:pk>/',DeportePerfilReservaDetallesAdmin.as_view(), name = 'reserva_detalles_deporte'),

	path('perfil_admin/reservas/hoteles/',PerfilListarReservasHotelesAdmin.as_view(), name='inicio_reservas_hoteles'),
	path('perfil_admin/listar_reservas_hoteles/', ListarReservasHotelesAdmin.as_view(), name = 'listar_reservas_hoteles'),
	path('perfil_admin/reserva_detalles_hotel/<int:pk>/',HotelPerfilReservaDetallesAdmin.as_view(), name = 'reserva_detalles_hotel'),

	path('perfil_admin/reservas/platos/',PerfilListarReservasPlatosAdmin.as_view(), name='inicio_reservas_platos'),
	path('perfil_admin/listar_reservas_platos/', ListarReservasPlatosAdmin.as_view(), name = 'listar_reservas_platos'),
	path('perfil_admin/reserva_detalles_plato/<int:pk>/',PlatoPerfilReservaDetallesAdmin.as_view(), name = 'reserva_detalles_plato'),

	path('perfil_admin/reservas/turismos/',PerfilListarReservasTurismosAdmin.as_view(), name='inicio_reservas_turismos'),
	path('perfil_admin/listar_reservas_turismos/', ListarReservasTurismosAdmin.as_view(), name = 'listar_reservas_turismos'),
	path('perfil_admin/reserva_detalles_turismo/<int:pk>/',TurismoPerfilReservaDetallesAdmin.as_view(), name = 'reserva_detalles_turismo'),

	#urls para reservas de user en perfil
	path('perfil/listar_mis_reservas/', ListarReservasUser.as_view(), name = 'listar_reservas_user_deportes'),
	path('perfil/reserva_detalles_deporte/<int:pk>/',DeportePerfilReservaDetallesUser.as_view(), name = 'reserva_detalles_user_deporte'),
]