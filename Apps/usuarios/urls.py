#creado manualmente
from django.urls import path
from django.contrib.auth.decorators import login_required
from Apps.usuarios.views import PerfilListarUsuario, RegistrarUsuario, ListarUsuario, EditarUsuario, EliminarUsuario, EditarUsuarioPassword, UsuarioPerfilDetalles

urlpatterns = [
	path('perfil_admin/usuarios/', PerfilListarUsuario.as_view(), name='inicio_usuarios'),
	path('perfil_admin/registrar_usuario/', RegistrarUsuario.as_view(), name = 'registrar_usuario'),
	path('perfil_admin/listar_usuarios/', ListarUsuario.as_view(), name = 'listar_usuario'),
	path('perfil_admin/detalles_usuario/<int:pk>/',UsuarioPerfilDetalles.as_view(), name = 'detalles_usuario'),
	path('perfil_admin/editar_usuario/<int:pk>/', EditarUsuario.as_view(), name = 'editar_usuario'),
	path('perfil_admin/editar_password_usuario/<int:pk>/', EditarUsuarioPassword.as_view(), name = 'editar_password_usuario'),
	path('perfil_admin/eliminar_usuario/<int:pk>/', EliminarUsuario.as_view(), name = 'eliminar_usuario'),
]