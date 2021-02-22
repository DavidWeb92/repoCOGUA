#archivo creado manualmente
from django import forms
from .models import Deporte

class DeporteForm(forms.ModelForm):
	class Meta:
		model = Deporte
		fields = ['nombre','precio','descripcion','cantidad','imagen']
		widgets = {
			'nombre': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'autocomplete': "off",
					'onfocus': "this.placeholder = ''",
					'onblur': "this.placeholder='Ingresar un nombre para el deporte'",
					'placeholder': 'Ingresar un nombre para el deporte',
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
					'onblur': "this.placeholder='Ingresar una descripcion para el depor'",
					'placeholder': 'Ingresar una descripcion para el deporte',
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
