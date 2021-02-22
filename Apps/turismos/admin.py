from django.contrib import admin
from .models import Turismo
# Register your models here.

class TurismoAdmin(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre','cantidad','precio','created','modified')

admin.site.register(Turismo,TurismoAdmin)