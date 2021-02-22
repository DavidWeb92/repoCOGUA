#archivo creado manualmente
from django import forms
from .models import Plato

class PlatoForm(forms.ModelForm):
	class Meta:
		model = Plato
		fields = ['nombre','precio','descripcion','cantidad','imagen']
		widgets = {
			'nombre': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'autocomplete': "off",
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='Ingresar un nombre para el Plato Tipico'",
					'placeholder': 'Ingresar un nombre para el Plato Tipico',
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
					'onblur': "this.placeholder='Ingresar una descripcion para el Plato Tipico'",
					'placeholder': 'Ingresar una descripcion para el Plato Tipico',
					'rows': 6,
					'cols': 30
				}
			),
			'cantidad': forms.NumberInput(
				attrs = {
					'class': 'form-control',
					'autocomplete': "off",
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='Ingresar una descripcion para el depor'",
					'placeholder': 'Ingresar una descripcion para el deporte'
				}
			)

		}
