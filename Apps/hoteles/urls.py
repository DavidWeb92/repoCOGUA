from django.urls import path
from .views import AgregarHotel, ListarHoteles, PerfilListarHoteles, HotelPerfilDetalles, EditarHotel, EliminarHotel

urlpatterns = [
	path('perfil_admin/agregar_hotel/',AgregarHotel.as_view(), name = 'agregar_hotel'),
	path('perfil_admin/cabañas/', PerfilListarHoteles.as_view(), name='inicio_hoteles'),
	path('perfil_admin/listar_cabañas/',ListarHoteles.as_view(), name = 'listar_hoteles'),
	path('perfil_admin/detalles_hotel/<int:pk>/',HotelPerfilDetalles.as_view(), name = 'detalles_hotel'),
	path('perfil_admin/editar_hotel/<int:pk>/',EditarHotel.as_view(), name = 'editar_hotel'),
	path('perfil_admin/eliminar_hotel/<int:pk>/',EliminarHotel.as_view(), name = 'eliminar_hotel'),
	
]