#archivo creado manualmente
from django.urls import path
from .views import Home, ListarDeportesDisponibles, DeporteDetalles, ListarHotelesDisponibles, ListarPlatosDisponibles, ListarTurismosDisponibles

urlpatterns = [
	path('',Home.as_view(), name='index'),
	path('home-deporte_detalles/<int:pk>/',DeporteDetalles.as_view(), name='deporte_detalles'),
	path('listado-deportes-disponibles/',ListarDeportesDisponibles.as_view(), name='listado_deportes_disponibles'),

	path('listado-cabañas-disponibles/',ListarHotelesDisponibles.as_view(), name='listado_hoteles_disponibles'),
	path('listado-platos-tipicos-disponibles/',ListarPlatosDisponibles.as_view(), name='listado_platos_disponibles'),
	path('listado-lugares-turisticos-disponibles/',ListarTurismosDisponibles.as_view(), name='listado_turismos_disponibles'),
]