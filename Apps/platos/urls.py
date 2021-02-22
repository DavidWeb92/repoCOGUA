from django.urls import path
from .views import AgregarPlato, ListarPlatos, PerfilListarPlatos, PlatoPerfilDetalles, EditarPlato, EliminarPlato

urlpatterns = [
	path('perfil_admin/agregar_plato/',AgregarPlato.as_view(), name = 'agregar_plato'),
	path('perfil_admin/platos/', PerfilListarPlatos.as_view(), name='inicio_platos'),
	path('perfil_admin/listar_platos/',ListarPlatos.as_view(), name = 'listar_platos'),
	path('perfil_admin/detalles_plato/<int:pk>/',PlatoPerfilDetalles.as_view(), name = 'detalles_plato'),
	path('perfil_admin/editar_plato/<int:pk>/',EditarPlato.as_view(), name = 'editar_plato'),
	path('perfil_admin/eliminar_plato/<int:pk>/',EliminarPlato.as_view(), name = 'eliminar_plato'),
	
]