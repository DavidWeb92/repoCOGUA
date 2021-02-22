from django.contrib import admin
from .models import ReservaDeporte, ReservaHotel, ReservaPlato, ReservaTurismo
# Register your models here.
class ReservaDeporteAdmin(admin.ModelAdmin):
	search_fields = ['usuario']
	readonly_fields=('usuario','deporte')
	list_display = ('usuario','deporte','fecha_inicial','fecha_final','created','modified')

class ReservaHotelAdmin(admin.ModelAdmin):
	search_fields = ['usuario']
	readonly_fields=('usuario','hotel')
	list_display = ('usuario','hotel','fecha_inicial','fecha_final','created','modified')

class ReservaPlatoAdmin(admin.ModelAdmin):
	search_fields = ['usuario']
	readonly_fields=('usuario','plato')
	list_display = ('usuario','plato','fecha_inicial','fecha_final','created','modified')

class ReservaTurismoAdmin(admin.ModelAdmin):
	search_fields = ['usuario']
	readonly_fields=('usuario','turismo')
	list_display = ('usuario','turismo','fecha_inicial','fecha_final','created','modified')
	
admin.site.register(ReservaTurismo, ReservaTurismoAdmin)
admin.site.register(ReservaDeporte, ReservaDeporteAdmin)
admin.site.register(ReservaHotel, ReservaHotelAdmin)
admin.site.register(ReservaPlato, ReservaPlatoAdmin)
