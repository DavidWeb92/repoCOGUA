"""Turismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#imports para las imagenes
from django.conf import settings
from django.views.static import serve
#fin imports de als imagenes
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
#from Apps.deportes.views import ListarDeporte
#from Apps.perfil.views import Perfil
from Apps.perfil.views import Login, logoutUsuario, RegistrarUser, LoginConfirmed

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #url para iniciar sesion despues de confirmar el email
    path('accounts-confirmed/login/', LoginConfirmed.as_view(), name = 'login_confirmed'),
    #urls para login
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    #urls para registrar usuario
    path('register/cogua/user/',RegistrarUser.as_view(), name='registrar_user'),
    #urls en general
    path('',include(('Apps.deportes.urls','templates_deporte'))),
    path('',include(('Apps.home.urls','templates_home'))),
    path('',include(('Apps.hoteles.urls','templates_hotel'))),
    path('',include(('Apps.perfil.urls','templates_perfil'))),
    path('',include(('Apps.platos.urls','templates_plato'))),
    path('',include(('Apps.reservas.urls','templates_reserva'))),
    path('',include(('Apps.turismos.urls','templates_turismo'))),
    path('',include(('Apps.usuarios.urls','templates_usuario'))),
    #urls necesarios para redirect(redireccionar)
    #path('perfil/listar_deporte/',login_required(ListarDeporte.as_view()), name='redirect_listar_deporte'),
    #path('perfil/',Perfil.as_view(), name='redirect_perfil'),
    #urls necesarios para reverse_lazy
    #path('perfil/',login_required(Perfil.as_view()), name='reverse_lazy_perfil'),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urls para caragr als imagenes
urlpatterns += [
    #esta urls es decir el re_path busca todos los archivos que estan en media, en este caso las imagenes
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
#fin urls
#linea para cambiar el de nombre de Administracion de Django por Administracion de CoGua
admin.site.site_header = 'Administración de CoGua'