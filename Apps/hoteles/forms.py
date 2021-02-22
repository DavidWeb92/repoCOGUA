#archivo creado manualmente
from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
	class Meta:
		model = Hotel
		fields = ['nombre','precio','descripcion','cantidad','imagen']
		widgets = {
			'nombre': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'autocomplete': "off",
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='Ingresar un nombre para la cabaña'",
					'placeholder': 'Ingresar un nombre para la cabaña',
					'id': 'nombre'
				}
			),
			'precio': forms.NumberInput(
				attrs = {
					'class': 'form-control',
					'autocomplete': "off",
					'step': 'any',
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='$'",
					'placeholder': '$'
				}
			),
			'descripcion': forms.Textarea(
				attrs = {
					'class': 'form-control',
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='Ingresar una descripcion para la cabaña'",
					'placeholder': 'Ingresar una descripcion para la cabaña',
					'rows': 6,
					'cols': 30
				}
			),
			'cantidad': forms.NumberInput(
				attrs = {
					'class': 'form-control',
					'autocomplete': "off",
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='Ingresar una descripcion la cabaña'",
					'placeholder': 'Ingresar una descripcion para la cabaña'
				}
			)

		}
