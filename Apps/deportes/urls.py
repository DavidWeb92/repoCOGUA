from django.urls import path
from .views import PerfilListarDeportes, AgregarDeporte, ListarDeporte, EditarDeporte, EliminarDeporte, DeportePerfilDetalles
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('perfil_admin/deportes/', PerfilListarDeportes.as_view(), name='inicio_deportes'),
	path('perfil_admin/agregar_deporte/',AgregarDeporte.as_view(), name = 'agregar_deporte'),
	path('perfil_admin/listar_deportes/',ListarDeporte.as_view(), name = 'listar_deporte'),
	path('perfil_admin/detalles_deporte/<int:pk>/',DeportePerfilDetalles.as_view(), name = 'detalles_deporte'),
	path('perfil_admin/editar_deporte/<int:pk>/',EditarDeporte.as_view(), name = 'editar_deporte'),
	path('perfil_admin/eliminar_deporte/<int:pk>/',EliminarDeporte.as_view(), name = 'eliminar_deporte'),
	
]