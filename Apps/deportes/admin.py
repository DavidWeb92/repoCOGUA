from django.contrib import admin
from .models import Deporte
# Register your models here.

class DeporteAdmin(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre','cantidad','precio','created','modified')

admin.site.register(Deporte,DeporteAdmin)