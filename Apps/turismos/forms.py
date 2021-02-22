#archivo creado manualmente
from django import forms
from .models import Turismo

class TurismoForm(forms.ModelForm):
	class Meta:
		model = Turismo
		fields = ['nombre','precio','descripcion','cantidad','imagen']
		widgets = {
			'nombre': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'autocomplete': "off",
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='Ingresar un nombre para el lugar turistico'",
					'placeholder': 'Ingresar un nombre para el lugar turistico',
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
					'onblur': "this.placeholder='Ingresar una descripcion para el lugar turistico'",
					'placeholder': 'Ingresar una descripcion para el lugar turistico',
					'rows': 6,
					'cols': 30
				}
			),
			'cantidad': forms.NumberInput(
				attrs = {
					'class': 'form-control',
					'autocomplete': "off",
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='Ingresar una descripcion para el lugar turistico'",
					'placeholder': 'Ingresar una descripcion para el lugar turistico'
				}
			)

		}
