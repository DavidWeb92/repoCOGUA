from django.contrib import admin
from .models import Plato
# Register your models here.

class PlatoAdmin(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre','cantidad','precio','created','modified')

admin.site.register(Plato,PlatoAdmin)