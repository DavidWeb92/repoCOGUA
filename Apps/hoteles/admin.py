from django.contrib import admin
from .models import Hotel
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre','cantidad','precio','created','modified')

admin.site.register(Hotel,HotelAdmin)