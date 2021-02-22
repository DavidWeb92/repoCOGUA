#archivo creado manualmente
from django.urls import path
from django.contrib.auth.decorators import login_required
from Apps.reservas.views import *

urlpatterns = [
	path('reservar-deporte/',RegistrarReservaDeporte.as_view(), name = 'reservar_deporte'),
	path('modal-reserva-deporte-detalles/<int:pk>/',ReservaDeporteDetalles.as_view(), name='modal_reserva_deporte_detalles'),
	path('perfil_admin/eliminar_reserva_deporte/<int:pk>/',EliminarReservaDeporte.as_view(), name = 'eliminar_reserva_deporte'),

	path('reservar-hotel/',RegistrarReservaHotel.as_view(), name = 'reservar_hotel'),
	path('modal-reserva-hotel-detalles/<int:pk>/',ReservaHotelDetalles.as_view(), name='modal_reserva_hotel_detalles'),
	path('perfil_admin/eliminar_reserva_hotel/<int:pk>/',EliminarReservaHotel.as_view(), name = 'eliminar_reserva_hotel'),

	path('reservar-plato/',RegistrarReservaPlato.as_view(), name = 'reservar_plato'),
	path('modal-reserva-plato-detalles/<int:pk>/',ReservaPlatoDetalles.as_view(), name='modal_reserva_plato_detalles'),
	path('perfil_admin/eliminar_reserva_plato/<int:pk>/',EliminarReservaPlato.as_view(), name = 'eliminar_reserva_plato'),

	path('reservar-turismo/',RegistrarReservaTurismo.as_view(), name = 'reservar_turismo'),
	path('modal-reserva-turismo-detalles/<int:pk>/',ReservaTurismoDetalles.as_view(), name='modal_reserva_turismo_detalles'),
	path('perfil_admin/eliminar_reserva_turismo/<int:pk>/',EliminarReservaTurismo.as_view(), name = 'eliminar_reserva_turismo'),

]