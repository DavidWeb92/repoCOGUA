from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Apps.deportes.models import Deporte
from Apps.hoteles.models import Hotel
from Apps.platos.models import Plato
from Apps.turismos.models import Turismo
# Create your views here.

class Home(TemplateView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['n_deportes'] = Deporte.objects.count()
		context['n_hoteles'] = Hotel.objects.count()
		context['n_platos'] = Plato.objects.count()
		context['n_turismos'] = Turismo.objects.count()
		return context

class DeporteDetalles(DetailView):
	model = Deporte
	template_name = 'home/index_DetallesDeportes.html'

class ListarDeportesDisponibles(ListView):
	model = Deporte
	paginate_by = 6
	template_name = 'home/deportes/index_ListarDeportesDisponibles.html'

	def get_queryset(self):
		queryset = self.model.objects.filter(cantidad__gte = 0)
		return queryset

class ListarHotelesDisponibles(ListView):
	model = Hotel
	paginate_by = 6
	template_name = 'home/hoteles/index_ListarHotelesDisponibles.html'

	def get_queryset(self):
		queryset = self.model.objects.filter(cantidad__gte = 0)
		return queryset

class ListarPlatosDisponibles(ListView):
	model = Plato
	paginate_by = 6
	template_name = 'home/platos/index_ListarPlatosDisponibles.html'

	def get_queryset(self):
		queryset = self.model.objects.filter(cantidad__gte = 0)
		return queryset

class ListarTurismosDisponibles(ListView):
	model = Turismo
	paginate_by = 6
	template_name = 'home/turismos/index_ListarTurismosDisponibles.html'

	def get_queryset(self):
		queryset = self.model.objects.filter(cantidad__gte = 0)
		return queryset

