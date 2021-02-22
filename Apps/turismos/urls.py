from django.urls import path
from .views import AgregarTurismo, ListarTurismos, PerfilListarTurismos, TurismoPerfilDetalles, EditarTurismo, EliminarTurismo

urlpatterns = [
	path('perfil_admin/agregar_turismo/',AgregarTurismo.as_view(), name = 'agregar_turismo'),
	path('perfil_admin/turismos/', PerfilListarTurismos.as_view(), name='inicio_turismos'),
	path('perfil_admin/listar_turismos/',ListarTurismos.as_view(), name = 'listar_turismos'),
	path('perfil_admin/detalles_turismo/<int:pk>/',TurismoPerfilDetalles.as_view(), name = 'detalles_turismo'),
	path('perfil_admin/editar_turismo/<int:pk>/',EditarTurismo.as_view(), name = 'editar_turismo'),
	path('perfil_admin/eliminar_turismo/<int:pk>/',EliminarTurismo.as_view(), name = 'eliminar_turismo'),
]